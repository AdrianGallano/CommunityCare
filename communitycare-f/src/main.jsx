import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {
  RouterProvider,
  createBrowserRouter,
  Navigate,
} from "react-router-dom";
import LogIn from "./components/Login.jsx";
import Map from "./components/Map.jsx";
import Signup from "./components/Signup";
import ErrorPage from "./components/ErrorPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Navigate to="/login" replace={true} />,
    errorElement: <ErrorPage />,
  },

  {
    path: "/login",
    element: <LogIn />,
  },

  {
    path: "/signup",
    element: <Signup />,
  },

  {
    path: "/map",
    element: <Map />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
