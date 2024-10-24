import CreateQrCode from "@/modules/qr-code/templates/new-qrcode"
import QRCodeList from "@/modules/qr-code/templates/qrcode-list"

export default function QRCode() {
    const data = [
        {
          "qrCodeId": "001",
          "restaurantName": "Bistro Cafe",
          "tableNumber": "10",
          "branch": "Main",
          "qrCodeUrl": "https://example.com/qr/001",
          "status": "Active",
          "creationDate": "2024-10-01",
          "expiryDate": "2025-10-01",
          "actions": ["Edit", "Delete"]
        },
        {
          "qrCodeId": "002",
          "restaurantName": "Bistro Cafe",
          "tableNumber": "11",
          "branch": "Main",
          "qrCodeUrl": "https://example.com/qr/002",
          "status": "Inactive",
          "creationDate": "2024-09-15",
          "expiryDate": null,
          "actions": ["Edit", "Delete"]
        },
        {
          "qrCodeId": "003",
          "restaurantName": "The Grill House",
          "tableNumber": "5",
          "branch": "Downtown",
          "qrCodeUrl": "https://example.com/qr/003",
          "status": "Active",
          "creationDate": "2024-08-25",
          "expiryDate": "2025-08-25",
          "actions": ["Edit", "Delete"]
        }
      ]
      
    return (
        <>
<CreateQrCode />        
        <QRCodeList qrcodes={data}/>
        </>
    )
}