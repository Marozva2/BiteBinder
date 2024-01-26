import React from "react";
import RecipeCard from "./RecipeCard";

const RecipeList = ({ meals, onGetRecipe }) => (
  <div id="meal">
    {meals.map((meal) => (
      <RecipeCard key={meal.idMeal} meal={meal} onGetRecipe={onGetRecipe} />
    ))}
  </div>
);

export default RecipeList;
