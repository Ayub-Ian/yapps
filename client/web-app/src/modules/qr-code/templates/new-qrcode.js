"use client";
import { useState } from "react";
import { cn } from "@/lib/utils";
import { Calendar } from "@/modules/common/components/ui/calendar";
import { Input } from "@/modules/common/components/ui/input";
import { format } from "date-fns"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/modules/common/components/ui/popover";
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/modules/common/components/ui/sheet";
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectLabel,
    SelectTrigger,
    SelectValue,
  } from "@/modules/common/components/ui/select"
import { CalendarIcon, QrCodeIcon } from "lucide-react";
import { Button } from "@/modules/common/components/ui/button";

export default function CreateQrCode() {
  const [date, setDate] = useState();

  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button className="bg-primary" >
        <QrCodeIcon className="mr-2 h-4 w-4" />
          New
        </Button>
      </SheetTrigger>
      <SheetContent>
        <SheetHeader>
          <SheetTitle>Create new QR Code</SheetTitle>
          <SheetDescription>
            Choose table to make QR Code here. Click generate when you're done.
          </SheetDescription>
        </SheetHeader>

        <form>
          <div className="grid w-full max-w-sm items-center gap-1.5">
            <label htmlFor="email">Title</label>
            <Input
              type="text"
              id="title"
              placeholder="i.e GrillMasters-Table10"
            />
          </div>

          <div className="grid w-full max-w-sm items-center gap-1.5">
            <label htmlFor="email">Table Number</label>
            <Input
              type="text"
              id="title"
              placeholder="i.e GrillMasters-Table10"
            />
          </div>
          <div className="grid w-full max-w-sm items-center gap-1.5">
            <label htmlFor="email">Branch</label>
            <Select>
      <SelectTrigger className="w-full">
        <SelectValue placeholder="Select a branch" />
      </SelectTrigger>
      <SelectContent>
        <SelectGroup>
          <SelectLabel>Branches</SelectLabel>
          <SelectItem value="apple">Apple</SelectItem>
          <SelectItem value="banana">Banana</SelectItem>
          <SelectItem value="blueberry">Blueberry</SelectItem>
          <SelectItem value="grapes">Grapes</SelectItem>
          <SelectItem value="pineapple">Pineapple</SelectItem>
        </SelectGroup>
      </SelectContent>
    </Select>
          </div>


          <div className="grid w-full max-w-sm items-center gap-1.5">
            <label htmlFor="email">Expiry date</label>
          <Popover>
            <PopoverTrigger asChild>
              <Button
              variant="outline"
                className={cn(
                  "w-full justify-start text-left font-normal ",
                  !date && "text-muted-foreground"
                )}
              >
                <CalendarIcon className="mr-2 h-4 w-4" />
                {date ? format(date, "PPP") : <span>Pick a date</span>}
              </Button>
            </PopoverTrigger>
            <PopoverContent className="w-auto p-0">
              <Calendar
                mode="single"
                selected={date}
                onSelect={setDate}
                initialFocus
              />
            </PopoverContent>
          </Popover>
          <span className="text-sm">The link will not work after selected date.</span>
          </div>

          <Button className="bg-primary">Generate QR Code</Button>
        </form>

        <SheetClose>
            <Button variant="ghost">Cancel</Button>
            </SheetClose>
      </SheetContent>
    </Sheet>
  );
}
