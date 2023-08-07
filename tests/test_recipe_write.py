"""
Automatic test of recipe manager write
"""
from pathlib import Path

# pylint: disable=E0401,W0601,W0611
from context import recipemanager
# pylint: disable=E0401
from context import recipe
# pylint: disable=E0401,W0611
from context import ingredient
# pylint: disable=E0401,C0411
from recipemanager import RecipeManager
# pylint: disable=E0401,C0411
from ingredient import Ingredient

path = Path("./testdata")


def pretty_print_recipe(_recipe: recipe.Recipe):
    """
    Allow simple printing of a recipe
    """
    print(
        str(f"Description: {_recipe.description} \n " +
            f"No. Servings: {_recipe.no_servings} \n " +
            f"Callories per portion: {_recipe.calories_per_portion} \n")
    )
    print("Ingredients:")
    for _ingredient in _recipe.ingredients:
        print(_ingredient.pretty_format())
    print("\nInstructions:")
    for instruction in _recipe.instructions:
        print(f"\n{instruction}")

path = Path("./testdata")

testrecipemanager = RecipeManager()

test_recipe = recipe.Recipe(title="Test recipe")
test_recipe.description = "A Test Recipe"
test_recipe.no_servings = 4
test_recipe.calories_per_portion = 250
test_recipe_ingredients = [
    Ingredient("Apple", 12.0, "Each", ["Apples"], 1136),
    Ingredient(
        "Plain Flour", 1000.0, "grammes", ["Wheat", "Cereals", "Gluten"], 2090
    ),
    Ingredient("Butter", 1400.0, "grammes", ["Dairy"], 10360),
    Ingredient("Honey", 8.0, "tbsp", ["Honey"], 512),
    Ingredient("Cinnamon", 4, "Pinch", [], 3),
    Ingredient("Mixed Spice", 4, "Pinch", [], 3),
    Ingredient("Beaten Egg", 4, "Each", ["Egg"], 360),
]

test_recipe.ingredients = test_recipe_ingredients

test_recipe.instructions = [
    str("STEP 1 - Heat oven to 200C/180C fan/gas 6. To make the pastry, sift " +
        "the flour into a large mixing bowl and add the butter or margarine. " +
        "Using your fingers, mix together until the mixture resembles " +
        "breadcrumbs."),
    str("STEP 2 - Add about 3 tbsp cold water – 1 tbsp at a time – to bind " +
        "the mixture into a ball. Then wrap it in cling film and leave to " +
        "chill in the fridge while you prepare the apples, or for 30 mins " +
        "if you have time."),
    str("STEP 3 - While the pastry is chilling, core the apples, then cut " +
        "into even-sized chunks so they all cook in the same amount of time. " +
        "Put the apples into the pie dish, drizzle over the honey and add the " +
        "cinnamon, mixed spice and about 2 tbsp water."),
    str("STEP 4 - Roll out the pastry on a floured work surface until it " +
        "is large enough to cover the pie dish. Using the rolling pin, " +
        "carefully lift the pastry and lay it over the top of the apple " +
        "mixture. Carefully trim off the excess pastry (this can be " +
        "rerolled and cut into shapes to decorate the pie crust if you " +
        "like) and press the pastry edges onto the dish to create a seal."),
    str("STEP 5 - Make a small cut in the pastry so that the air can " +
        "escape during cooking, then brush with beaten egg to glaze."),
    str("STEP 6 - Bake the pie in the oven for 20-30 mins until the " +
        "pastry is golden and sandy in appearance and the apple filling " +
        "is bubbling and hot."),
]

testrecipemanager.add_recipe(test_recipe)

RecipeManager.write_recipe_to_file(recipe=test_recipe,directory_path=path)
