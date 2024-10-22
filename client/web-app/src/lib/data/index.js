import { API_SERVER_BASE_URL } from "../config";
import { cookies } from "next/headers";

async function authenticate(credentials, customHeaders = null) {
  
    const res = await fetch(`${API_SERVER_BASE_URL}/api/login/`, {
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

    return data

}



export async function getToken(credentials) {
  return authenticate(credentials)  
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
