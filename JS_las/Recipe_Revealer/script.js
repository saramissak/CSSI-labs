// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

const recipe = [];


const addInstructions = () => {
  // add all of the instructions into the recipeArray variable
  recipe.push("1. Heat oven to 425ºF. Prepare Double-Crust Pastry.")
  recipe.push("2. Mix sugar, flour, cinnamon, nutmeg and salt in large bowl.")
  recipe.push("3. Stir in apples.")
  recipe.push("4. Turn into pastry-lined pie plate. Dot with butter. Trim overhanging edge of pastry 1/2 inch from rim of plate.")
  recipe.push("5. Roll other round of pastry. Fold into fourths and cut slits so steam can escape.")
  recipe.push("6. Unfold top pastry over filling; trim overhanging edge 1 inch from rim of plate.")
  recipe.push("7. Fold and roll top edge under lower edge, pressing on rim to seal; flute as desired.")
  recipe.push("8. Cover edge with 3-inch strip of aluminum foil to prevent excessive browning. Remove foil during last 15 minutes of baking.")
  recipe.push("9. Bake 40 to 50 minutes or until crust is brown and juice begins to bubble through slits in crust. Serve warm if desired.")
  // return the array
  return recipe;
};

const checkStep = (stepToCheck) => {
  return recipe[stepToCheck-1]
};

function checkLength(array){
  return array.length;
}


addInstructions()
checkStep(1)
checkLength(recipe)
// Write a function publishRecipe
