
import { useState, useEffect } from "react";
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
  const [userData, setUserData] = useState({
    username: "",
    password: ""
  });

  const [token, setToken] = useState(null);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData({
      ...userData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log(userData);
      const response = await fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const jsonData = await response.json();
      setToken(jsonData.access);
      localStorage.setItem('accessToken', `Bearer ${jsonData.access}`);
    } catch (error) {
      setError(error);
      throw error;
    }
  };

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
              Enter your username below to login to your account
            </CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit}>
              <div className="grid gap-4">
                <div className="grid gap-2">
                  <Label htmlFor="username">username</Label>
                  <Input
                    id="username"
                    type="text"
                    name="username"
                    placeholder="Megatron3000"
                    onChange={handleInputChange}
                    autoComplete="username"
                    required
                  />
                </div>
                <div className="grid gap-2">
                  <div className="flex items-center">
                    <Label htmlFor="password">Password</Label>
                  </div>
                  <Input
                    id="password"
                    type="password"
                    name="password"
                    placeholder="************"
                    onChange={handleInputChange}
                    autoComplete="current-password"
                    required
                  />
                </div>
                <Button type="submit" className="w-full">
                  Login
                </Button>
              </div>
            </form>
            <div className="mt-4 text-center text-sm">
              Don't have an account?{" "}
              <Link to={"/signup"}> Register here</Link>
            </div>
          </CardContent>
        </Card>
      </div>
    </>
  );
};

export default LogIn;
