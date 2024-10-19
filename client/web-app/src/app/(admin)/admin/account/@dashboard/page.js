import { Metadata } from "next";

// import { getCustomer, listCustomerOrders } from "@lib/data"
// import Overview from "@modules/account/components/overview"
import { notFound } from "next/navigation";

export const metadata = {
  title: "Account",
  description: "Overview of your account activity.",
};

export default async function OverviewTemplate() {
  // const customer = await getCustomer().catch(() => null)
  // const orders = (await listCustomerOrders().catch(() => null)) || null
  const customer = true;

  if (!customer) {
    notFound();
  }

  return <>Hello</>;
}
