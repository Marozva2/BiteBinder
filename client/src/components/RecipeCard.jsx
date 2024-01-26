import React from "react";

const RecipeCard = ({ meal, onGetRecipe }) => (
  <div className="meal-item" onClick={() => onGetRecipe(meal.idMeal)}>
    <div className="meal-img">
      <img src={meal.strMealThumb} alt="food" />
    </div>
    <div className="meal-name">
      <h3>{meal.strMeal}</h3>
      <button>Get Recipe</button>
    </div>
  </div>
);

export default RecipeCard;
