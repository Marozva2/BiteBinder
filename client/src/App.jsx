import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MealApp from "./components/MealApp";
import Authentication from "./components/Authentication"
import Home from "./components/Home";
import NavBar from "./components/NavBar";

function App() {
  return (
    <Router>
      <NavBar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/mealapp" element={<MealApp />} />
        <Route path="/signin" element={<Authentication />} />
        <Route path="/signup" element={<Authentication />} />
      </Routes>
    </Router>
  );
}

export default App;
