import Link from "next/link";

export default function AdminNav({ children }) {
  return (
    <div className="flex-col md:flex-row flex">
      <div className="hidden md:flex w-64 flex-col">
      <Link href="/admin/menu">
            Menu
            </Link>
            <Link href="/admin/qr-code">
            QR Code
            </Link>
      </div>
      <main>
        <div>top nav</div>
        <div>{children}</div>
      </main>
    </div>
  );
}
