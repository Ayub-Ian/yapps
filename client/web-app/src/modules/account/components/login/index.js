"use client";

import { useFormState } from "react-dom";

import { SubmitButton } from "@/modules/common/components/submit-button";
import { Input } from "@/modules/common/components/ui/input";

import { logCustomerIn } from "@/modules/account/actions";
// import ErrorMessage from "@modules/checkout/components/error-message"

const Login = () => {
  const [message, formAction] = useFormState(logCustomerIn, null);

  return (
    <div
      className="max-w-sm w-full flex flex-col items-center"
      data-testid="login-page"
    >
      <h1 className="text-large-semi uppercase mb-6">Welcome back</h1>
      <p className="text-center text-base-regular text-ui-fg-base mb-8">
        Sign in to access an enhanced dining experience.
      </p>
      <form className="w-full" action={formAction}>
        <div className="flex flex-col w-full gap-y-2">
          <label htmlFor="email" className="flex flex-col gap-1">
            Email
            <Input
              id="email"
              name="email"
              type="email"
              placeholder="Enter a valid email address."
              autoComplete="email"
              required
              data-testid="email-input"
            />
          </label>

          <label htmlFor="password" className="flex flex-col gap-1">
            Password
            <Input
              id="password"
              name="password"
              type="password"
              placeholder="Secure password"
              autoComplete="current-password"
              required
              data-testid="password-input"
            />
          </label>
        </div>
        {/* <ErrorMessage error={message} data-testid="login-error-message" /> */}
        <SubmitButton
          data-testid="sign-in-button"
          className="w-full mt-6 bg-primary text-white font-medium rounded-xl"
        >
          Sign in
        </SubmitButton>
      </form>
    </div>
  );
};

export default Login;
