import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import MealApp from "./MealApp";
import SignIn from "./SignIn";
import SignUp from "./SignUp";
import "/src/index.css"

const NavBar = () => (
  <nav className="bg-blue-800 p-2">
    <ul className="flex justify-between text-white">
      <li className="mx-2">
        <Link to="/" className="hover:underline">
          Home
        </Link>
      </li>
      <li className="mx-2">
        <Link to="/mealapp" className="hover:underline">
          MealApp
        </Link>
      </li>
      <li className="mx-2">
        <Link to="/signin" className="hover:underline">
          Sign In
        </Link>
      </li>
      <li className="mx-2">
        <Link to="/signup" className="hover:underline">
          Sign Up
        </Link>
      </li>
    </ul>
  </nav>
);

export default NavBar;
