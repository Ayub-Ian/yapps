
import AccountLayout from "@/modules/account/templates/account-layout";

export default async function AccountPageLayout({ dashboard }) {


  return (
    <AccountLayout>
      {dashboard }
    </AccountLayout>
  );
}
