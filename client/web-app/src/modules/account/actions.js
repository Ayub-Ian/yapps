"use server";

import { signIn } from "@/lib/auth";
import { AuthError } from "next-auth";
import { revalidateTag } from "next/cache";
import { z } from "zod";

export async function authenticate(_currentState, formData) {
 
  const validatedFields = z
    .object({
      email: z
        .string({
          invalid_type_error: "Invalid Email",
        })
        .email(),
    })
    .safeParse({
      email: formData.get("email"),
    });

  // Return early if the form data is invalid
  if (!validatedFields.success) {
    return {
      errors: validatedFields.error.flatten().fieldErrors,
    };
  }

  try {
    await signIn("credentials", formData);
    revalidateTag("auth")
  } catch (error) {
    if (error instanceof AuthError) {
      switch (error.type) {
        case "CredentialsSignin":
          return "Invalid credentials.";
        default:
          return "Something went wrong.";
      }
    }
    throw error;
  }
}
