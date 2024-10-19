"use client";

import { useFormStatus } from "react-dom";
import { Button } from "../ui/button";
import { Loader2Icon } from "lucide-react";

export function SubmitButton({
  children,
  variant = "primary",
  className,
  "data-testid": dataTestId,
}) {
  const { pending } = useFormStatus();

  return (
    <Button
      className={className}
      type="submit"
      disabled={pending}
      variant={variant}
      data-testid={dataTestId}
    >
      {pending && <Loader2Icon className="mr-2 h-4 w-4 animate-spin" />}
      {children}
    </Button>
  );
}
