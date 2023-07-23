import sys

sys.path.append("../")
from recipe import Recipe
from ingredient import Ingredient


def pretty_print_recipe(recipe: Recipe):
    print(
        f"Description: {recipe.description} \n No. Servings: {recipe.no_servings} \n Callories per portion: {recipe.calories_per_portion} \n"
    )
    print("Ingredients:")
    for ingredient in recipe.ingredients:
        print(ingredient.pretty_format())
    print("\nInstructions:")
    for instruction in recipe.instructions:
        print(f"\n{instruction}")


apple_pie_recipe = Recipe(title="Apple Pie")
apple_pie_recipe.description = "Simple Traditional Apple Pie Recipe"
apple_pie_recipe.no_servings = 12
apple_pie_recipe.calories_per_portion = 250
apple_pie_ingredients = [
    Ingredient("Apple", 12.0, "Each", ["Apples"], 1136),
    Ingredient("Plain Flour", 1000.0, "grammes", ["Wheat", "Cereals", "Gluten"], 2090),
    Ingredient("Butter", 1400.0, "grammes", ["Dairy"], 10360),
    Ingredient("Honey", 8.0, "tbsp", ["Honey"], 512),
    Ingredient("Cinnamon", 4, "Pinch", [], 3),
    Ingredient("Mixed Spice", 4, "Pinch", [], 3),
    Ingredient("Beaten Egg", 4, "Each", ["Egg"], 360),
]

apple_pie_recipe.ingredients = apple_pie_ingredients

apple_pie_recipe.instructions = [
        "STEP 1 - Heat oven to 200C/180C fan/gas 6. To make the pastry, sift the flour into a large mixing bowl and add the butter or margarine. Using your fingers, mix together until the mixture resembles breadcrumbs.",
        "STEP 2 - Add about 3 tbsp cold water – 1 tbsp at a time – to bind the mixture into a ball. Then wrap it in cling film and leave to chill in the fridge while you prepare the apples, or for 30 mins if you have time.",
        "STEP 3 - While the pastry is chilling, core the apples, then cut into even-sized chunks so they all cook in the same amount of time. Put the apples into the pie dish, drizzle over the honey and add the cinnamon, mixed spice and about 2 tbsp water.",
        "STEP 4 - Roll out the pastry on a floured work surface until it is large enough to cover the pie dish. Using the rolling pin, carefully lift the pastry and lay it over the top of the apple mixture. Carefully trim off the excess pastry (this can be rerolled and cut into shapes to decorate the pie crust if you like) and press the pastry edges onto the dish to create a seal.",
        "STEP 5 - Make a small cut in the pastry so that the air can escape during cooking, then brush with beaten egg to glaze.",
        "STEP 6 - Bake the pie in the oven for 20-30 mins until the pastry is golden and sandy in appearance and the apple filling is bubbling and hot.",
    ]

# Print out the recipe
pretty_print_recipe(apple_pie_recipe)
