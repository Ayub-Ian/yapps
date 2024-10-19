"use server";

// import { getToken } from "@lib/data";
import { revalidateTag } from "next/cache";
import { redirect } from "next/navigation";
import { cookies, headers } from "next/headers";

export async function logCustomerIn(_currentState, formData) {
  const email = formData.get("email");
  const password = formData.get("password");

  // try {
  //   await getToken({ email, password }).then(() => {
  //     revalidateTag("customer")
  //   })
  // } catch (error) {
  //   return error.toString()
  // }
}
