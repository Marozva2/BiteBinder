import React from "react";
import image from "/src/assets/recipe.jpg";

const Hero = () => {
  return (
    <div className="container mx-auto">
      <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 px-28">
        <div className="mt-28">
          <h1 className="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl ">
            Discover New Recipes and Flavors
          </h1>
          <p className="mb-6 text-lg font-normal text-gray-500 lg:text-xl">
            Explore a variety of recipes from around the world. <br />
            Cook at your own pace, from the comfort of your home.
          </p>
          <a
            href="/mealapp"
            className="inline-flex items-center px-10 py-2 text-sm font-medium text-center text-blue-500 border-2 border-blue-500 rounded-lg "
          >
            Explore Recipes
            <svg
              className="w-3.5 h-3.5 ml-2"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M1 5h12m0 0L9 1m4 4L9 9"
              />
            </svg>
          </a>
        </div>
        <div>
          <img
            className="h-auto max-w-full rounded-lg"
            src={image}
            alt="Recipe book"
          />
        </div>
      </div>
    </div>
  );
};

export default Hero;
