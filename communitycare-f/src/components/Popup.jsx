import React from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

const Popup = ({ barangay }) => {
  return (
    <Card className="border-0 shadow-none">
      <CardHeader>
        <CardTitle>{barangay.name}</CardTitle>
      </CardHeader>
      <CardContent>
        <Sheet>x
          <SheetTrigger asChild>
            <Button>More Information</Button>
          </SheetTrigger>
          <SheetContent>
            <SheetHeader>
              <SheetTitle>Barangay Information</SheetTitle>
            </SheetHeader>
            <SheetDescription>
              <span className="font-mono font-bold text-lg">
                {barangay.name}
              </span>
              <span>Latitude: {barangay.gps.latitude}</span>
              <span>Longitude: {barangay.gps.longitude}</span>
            </SheetDescription>
            <SheetFooter>
              <SheetClose asChild>
                <Button type="submit">Save changes</Button>
              </SheetClose>
            </SheetFooter>
          </SheetContent>
        </Sheet>
      </CardContent>
    </Card>
  );
};

export default Popup;
