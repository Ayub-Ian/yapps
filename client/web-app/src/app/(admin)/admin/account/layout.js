// import { getCustomer } from "@lib/data"

import AccountLayout from "@/modules/account/templates/account-layout";

export default async function AccountPageLayout({ dashboard, login }) {
  // const customer = await getCustomer().catch(() => null)
  const customer = false;

  return (
    <AccountLayout customer={customer}>
      {customer ? dashboard : login}
    </AccountLayout>
  );
}
