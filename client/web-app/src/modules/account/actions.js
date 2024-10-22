"use server";

// import { getToken } from "@lib/data";
import { revalidateTag } from "next/cache";
import { redirect } from "next/navigation";
import { cookies, headers } from "next/headers";

export async function authenticate(_currentState, formData) {
  const email = formData.get("email");
  const password = formData.get("password");

  try {
    // await getToken({ email, password }).then(() => {
    //   revalidateTag("customer")
    // })
    await signStaffIn('credentials', formData)
  } catch (error) {
    if (error instanceof AuthError) {
      switch (error.type) {
        case 'CredentialsSignin':
          return 'Invalid credentials.';
        default:
          return 'Something went wrong.';
      }
    }
    throw error;
  }

  }
}
