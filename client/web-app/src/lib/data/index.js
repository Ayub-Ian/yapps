import { useMutation } from "@tanstack/react-query";

async function useAuthenticate(credentials, customHeaders = null) {
  return useMutation(async (credentials) => {
    const res = await fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(credentials),
      next: { tags: ["auth"] }, // Adding cache tag 'auth'
    });

    if (!res.ok) {
      throw new Error("Login failed");
    }

    const data = await res.json();
    return data.jwt_token; // Assuming API returns a JWT token
  });
}
export async function getToken(credentials) {
  return medusaClient.auth
    .getToken(credentials, {
      next: {
        tags: ["auth"],
      },
    })
    .then(({ access }) => {
      access &&
        cookies().set("_yapps_jwt", access, {
          maxAge: 60 * 60 * 24 * 7,
          httpOnly: true,
          sameSite: "strict",
          secure: process.env.NODE_ENV === "production",
        });
      return access;
    })
    .catch((err) => {
      throw new Error("Wrong email or password.");
    });
}
