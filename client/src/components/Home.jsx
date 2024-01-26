import React from "react";
import Testimonials from "./Testimonials.jsx";
import Hero from "./Hero.jsx";
import Footer from "./Footer.jsx";

function Home() {
  return (
    <div>
      <h1>Welcome to BiteBinders</h1>
      <Hero />
      <Testimonials />
      <Footer />
    </div>
  );
}

export default Home;
