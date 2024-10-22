import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { jwtDecode } from "jwt-decode";
import { authConfig } from "./config";
import { getToken } from "./data";

/**
 * Takes a token, and returns a new token with updated
 * `accessToken` and `accessTokenExpires`. If an error occurs,
 * returns the old token and an error property
 */
async function refreshAccessToken(token) {
  try {
    const response = await fetch(
      `${process.env.API_SERVER_BASE_URL}/api/refresh`,
      {
        headers: {
          Authorization: `Bearer ${token.refreshToken}`,
        },
      }
    );

    const tokens = await response.json();

    if (!response.ok) {
      throw tokens;
    }

    return {
      ...token,
      accessToken: tokens.accessToken,
      refreshToken: tokens.refreshToken ?? token.refreshToken, // Fall back to old refresh token
    };
  } catch (error) {
    console.log(error);

    return {
      ...token,
      error: "RefreshAccessTokenError",
    };
  }
}

export const { auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      async authorize(credentials) {
        if (credentials) {
          const parsedData = await getToken(credentials);
          if (!parsedData) return null;

          const accessToken = parsedData.access;
          const refreshToken = parsedData.refresh;
          

          return {
            accessToken,
            refreshToken,
          };
        }

        return null;
      },
    }),
  ],
  callbacks: {
    jwt: async ({ token, account, user }) => {
      // user is only available the first time a user signs in authorized
      if (token.accessToken) {
        const decodedToken = jwtDecode(token.accessToken);
        token.accessTokenExpires = decodedToken?.exp * 1000;
      }

      if (account && user) {
        return {
          ...token,
          accessToken: user.accessToken,
          refreshToken: user.refreshToken,
          user,
        };
      }

      // Return previous token if the access token has not expired yet

      if (Date.now() < token.accessTokenExpires) {
        return token;
      }

      // Access token has expired, try to update it
      //return token;
      return refreshAccessToken(token);
    },
    session: async ({ session, token }) => {
      if (token) {
        session.accessToken = token.accessToken;
        session.user = token.user;
      }
      return session;
    },
  },
});
