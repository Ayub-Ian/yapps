import AdminNav from "@/modules/layout/admin/templates";

export default function DashboardLayout({ children }) {
  return <><AdminNav>{children}</AdminNav></>;
}
