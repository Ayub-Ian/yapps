import AdminNav from "@/modules/layout/admin/templates";

export default function AdminRootLayout({ children }) {
    return (
        <>
        <AdminNav>{children}</AdminNav>
        
        </>
    )
}