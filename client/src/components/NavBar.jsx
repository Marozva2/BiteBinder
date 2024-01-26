import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "/src/index.css";

const NavBar = () => (
  <nav className="ui raised segment center aligned">
    <ul className="flex justify-between text-white">
      <li className="mx-2">
        <Link to="/" className="hover:underline">
          Home
        </Link>
      </li>
      <li className="mx-2">
        <Link to="/mealapp" className="hover:underline">
          Meals
        </Link>
      </li>
      <li className="mx-2">
        <Link to="/signin" className="hover:underline">
          Sign In
        </Link>
      </li>
    </ul>
  </nav>
);

export default NavBar;
