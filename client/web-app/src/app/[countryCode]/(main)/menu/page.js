import Image from "next/image";
import Link from "next/link";

async function retrieveRestaurantMenus() {
  const res = await fetch("http://127.0.0.1:8000/api/restaurants/1/menus");

  if (!res.ok) throw new Error("Failed to fetch data");

  return res.json();
}

export default async function MenuPage() {
  const data = await retrieveRestaurantMenus();

  return (
    <>
      <h3>Select Menu</h3>
      <div className="grid grid-cols-2">
        {data.map((data) => {
          return (
            <Link key={data.id} href="#">
              <div className="relative">
                {data.image_url && (
                  <Image
                    src={
                      "https://cdn.pixabay.com/photo/2017/08/02/00/51/food-2569257_1280.jpg"
                    }
                    alt="menu"
                    width={80}
                    height={80}
                  />
                )}
              </div>
              <h2>{data.name}</h2>
            </Link>
          );
        })}
      </div>
    </>
  );
}
