import React, { useState } from "react";
import SearchBar from "./SearchBar";
import RecipeList from "./RecipeList";
import Recipe from "./Recipe";

const MealApp = () => {
  const [mealList, setMealList] = useState([]);
  const [showRecipe, setShowRecipe] = useState(false);
  const [mealDetails, setMealDetails] = useState({});

  const getMealList = (searchInputTxt) => {
    fetch(
      `https://www.themealdb.com/api/json/v1/1/filter.php?i=${searchInputTxt}`
    )
      .then((response) => response.json())
      .then((data) => {
        if (data.meals) {
          setMealList(data.meals);
        } else {
          setMealList([]);
        }
      });
  };

  const getMealRecipe = (id) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
      .then((response) => response.json())
      .then((data) => {
        setMealDetails(data.meals[0]);
        setShowRecipe(true);
      });
  };

  return (
    <div>
      <SearchBar onSearch={getMealList} />
      <RecipeList meals={mealList} onGetRecipe={getMealRecipe} />
      {showRecipe && <Recipe meal={mealDetails} />}
    </div>
  );
};

export default MealApp;
