import React from "react";
import RecipeCard from "./RecipeCard";

const RecipeList = ({ meals, onGetRecipe }) => (
  <div className="ui divided four column grid">
    {meals.map((meal) => (
      <div className="column" key={meal.idMeal}>
        <RecipeCard meal={meal} onGetRecipe={onGetRecipe} />
      </div>
    ))}
  </div>
);

export default RecipeList;
