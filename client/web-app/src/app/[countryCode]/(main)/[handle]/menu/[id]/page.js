import { CircleAlertIcon } from "lucide-react";
import Image from "next/image";

async function getMenuItemsById(id) {
  const res = await fetch("");
}

export default async function MenuItemPage() {
  const menuItems = [
    {
      "name": "Grilled Chicken Sandwich",
      "description": "Juicy grilled chicken breast served with lettuce, tomato, and a spicy mayo on a toasted bun.",
      "price": 9.99,
      "currency": "USD"
    },
    {
      "name": "BBQ Ribs",
      "description": "Tender baby back ribs glazed with our signature BBQ sauce, served with coleslaw.",
      "price": 14.99,
      "currency": "USD"
    },
    {
      "name": "Veggie Burger",
      "description": "A flavorful black bean burger topped with avocado, sprouts, and a zesty aioli.",
      "price": 8.99,
      "currency": "USD"
    },
    {
      "name": "Steak Frites",
      "description": "Grilled ribeye steak served with crispy fries and a side of garlic butter.",
      "price": 19.99,
      "currency": "USD"
    },
    {
      "name": "Caesar Salad",
      "description": "Crisp romaine lettuce tossed with Caesar dressing, croutons, and parmesan cheese.",
      "price": 7.99,
      "currency": "USD"
    },
    {
      "name": "Margarita Pizza",
      "description": "Classic pizza topped with fresh mozzarella, basil, and tomato sauce.",
      "price": 11.99,
      "currency": "USD"
    },
    {
      "name": "Chocolate Lava Cake",
      "description": "Warm chocolate cake with a gooey center, served with vanilla ice cream.",
      "price": 6.99,
      "currency": "USD"
    },
    {
      "name": "Lemonade",
      "description": "Refreshing homemade lemonade, served chilled.",
      "price": 2.99,
      "currency": "USD"
    }
  ]
  
  
  return (
    <>
      <div className="w-full relative h-52 justify-end flex flex-col bg-gray-800 px-4">
        <div
          className="absolute inset-0 bg-cover bg-center transition-opacity duration-500"
          style={{
            backgroundImage:
              "url('https://cdn.pixabay.com/photo/2016/11/18/14/05/brick-wall-1834784_1280.jpg')",
            backgroundColor: "gray",
          }}
        >
          <div className="absolute inset-0 bg-black opacity-50"></div>
        </div>


        <div className="flex relative flex-col z-10 text-white mb-2">
          <h1 className="font-semibold mb-1 text-xl">Connie's Restaurant</h1>
          <p className="text-balance ">
            Traditional italian lorem ipsum and more cousine from those who
            brought you La Marina
          </p>

          <div className="my-2 flex items-center">
            <CircleAlertIcon className="mr-1 h-4 w-4" />
            <p className="font-medium ">About</p>
          </div>
        </div>
      </div>

      <div className="px-4">

      <h2 className="text-lg font-bold mb-3">Brunch</h2>


      <ul className="flex flex-col space-y-4 divide-y">
        {menuItems.map((item) => {
          return (
            <li key={item.name} className="flex pt-2">
              <div className="text-balance text-ellipsis flex-1 mr-2">
              <h1 className="font-semibold mb-1">{item.name}</h1>
              <p className="text-sm mb-2">{item.description}</p>
              <div className="flex items-end space-x-1 leading-none">
                <span className="text-xs">{item.currency}</span>
                <p  >{item.price}</p>
              </div>
              
              </div>
              <div className="h-24 w-24 rounded-md bg-gray-800"></div>
            </li>
          )
        })}
      </ul>
      </div>
    </>
  );
}
