import { Table, Tbody, Tcell, Thead, Trow } from "@/modules/common/components/table";
import Link from "next/link";

export default function QRCodeList({ qrcodes }){
    return (
        <>
        <Table>
            <Thead>
                <Tcell>QR Code ID</Tcell>
                <Tcell>Table Number</Tcell>
                <Tcell>Branch</Tcell>
                <Tcell>URL</Tcell>
                <Tcell>Status</Tcell>
                <Tcell>Creation Date</Tcell>
                <Tcell>Expiry Date</Tcell>
            </Thead>
            <Tbody>
                {qrcodes?.map((qrcode) => {
                    const { qrCodeId, qrCodeUrl, tableNumber, creationDate, expiryDate, branch, status } = qrcode
                    return (
                        <Trow key={qrCodeId}>
                            <Tcell>{qrCodeId}</Tcell>
                            <Tcell>{tableNumber}</Tcell>
                            <Tcell>{branch}</Tcell>
                            <Tcell>
                                <Link href={qrCodeUrl}>View URL</Link>
                            </Tcell>
                            <Tcell>{status}</Tcell>
                            <Tcell>{creationDate}</Tcell>
                            <Tcell>{expiryDate}</Tcell>
                        </Trow>
                    )
                })}
            </Tbody>
            </Table></>
    )
}