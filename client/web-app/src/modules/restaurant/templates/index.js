import { Button } from "@/modules/common/components/ui/button";
import Image from "next/image";
import Link from "next/link";

export default function HomePage() {
  return (
    <div className="h-screen">
      <div className="flex h-full flex-col">
        <div className="flex-grow flex items-center flex-col pt-10 text-center">
          <div className="relative h-20 w-20 mb-4">
            <Image
              src="https://cdn.pixabay.com/photo/2014/04/02/16/23/coffee-307147_960_720.png"
              alt="grill masters logo"
              fill
            />
          </div>
          <h1 className="font-semibold text-lg">Grill Masters</h1>
        </div>

        <div className="flex flex-col items-center mb-4">
          <div className="w-52 text-center mb-4">
            <p className="font-medium text-lg">
              Please choose your desired action
            </p>
          </div>

          <div className="flex flex-col w-full px-8 pb-36 space-y-4">
            
            <Link href="/ke/grill/menu/1"> 
            <Button variant="outline" className="w-full text-primary rounded-xl font-medium" >View Menu</Button></Link>
          
          <Button className="w-full bg-primary rounded-xl font-medium">Pay Bill</Button>
          </div>

          <footer className="text-xs ">Crafted experience by Yapps.</footer>
        </div>
      </div>
    </div>
  );
}
