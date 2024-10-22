import {
  QueryClient,
  defaultShouldDehydrateQuery,
  isServer,
} from "@tanstack/react-query";

export let API_SERVER_BASE_URL = "http://localhost:8000";

if (process.env.NEXT_PUBLIC_API_SERVER_BASE_URL) {
  API_SERVER_BASE_URL = process.env.NEXT_PUBLIC_API_SERVER_BASE_URL;
}

function makeQueryClient() {
  return new QueryClient({
    defaultOptions: {
      queries: {
        staleTime: 60 * 1000,
      },
      dehydrate: {
        // include pending queries in dehydration
        shouldDehydrateQuery: (query) =>
          defaultShouldDehydrateQuery(query) ||
          query.state.status === "pending",
      },
    },
  });
}

let browserQueryClient = undefined;

export function getQueryClient() {
  if (isServer) {
    // Server: always make a new query client
    return makeQueryClient();
  } else {
    // Browser: make a new query client if we don't already have one
    // This is very important, so we don't re-make a new client if React
    // suspends during the initial render. This may not be needed if we
    // have a suspense boundary BELOW the creation of the query client
    if (!browserQueryClient) browserQueryClient = makeQueryClient();
    return browserQueryClient;
  }
}

export const authConfig = {
  pages: {
    signIn: "/staff/login",
  },
  session: {
    strategy: 'jwt',
    maxAge: 24 * 60 * 60, // 1 Day
   },
  callbacks: {
    authorized({ auth, request: { nextUrl } }) {
      const isLoggedIn = !!auth?.user;
      const isOnAdmin = nextUrl.pathname.startsWith("/staff");
      if (isOnAdmin) {
        if (isLoggedIn) return true;
        return false; // Redirect unauthenticated users to login page
      } else if (isLoggedIn) {
        return Response.redirect(new URL("/staff", nextUrl));
      }
      return true;
    },
  },
  providers: [], // Add providers
};
