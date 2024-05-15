import LogInService from "./../services/LoginService";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const LogIn = () => {
  let token = LogInService();
  console.log(token);

  return (
    <>
      <div className="flex justify-center items-center h-screen">
        <Card className="mx-auto w-[30%] max-sm:w-fit max-sm:my-5">
          <CardHeader>
            <CardTitle className="text-xl text-center">
              {" "}
              Welcome to CommunityCare
            </CardTitle>
            <CardDescription className="text-xs text-center">
              Enter your email below to login to your account
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form>
              <div className="grid gap-4">
                <div className="grid gap-2">
                  <Label htmlFor="email">Email</Label>
                  <Input
                    id="email"
                    type="email"
                    placeholder="example@gmail.com"
                    required
                  />
                </div>
                <div className="grid gap-2">
                  <div className="flex items-center">
                    <Label htmlFor="password">Password</Label>
                  </div>
                  <Input id="password" type="password" required />
                </div>
                <Button type="submit" className="w-full">
                  Login
                </Button>
              </div>
            </form>
            <div className="mt-4 text-center text-sm">
              Don&apos;t have an account?{" "}
              <Link to={"/signup"}> Register here</Link>
            </div>
          </CardContent>
        </Card>
      </div>
    </>
  );
};

export default LogIn;
