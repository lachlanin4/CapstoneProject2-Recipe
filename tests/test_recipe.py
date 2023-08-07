"""
This is a basic test of recipe
"""
# pylint: disable=E0401
from context import recipe
# pylint: disable=E0401
from context import ingredient


def pretty_print_recipe(_recipe: recipe.Recipe):
    """
    Print the recipe
    """
    print(
        f"Description: {_recipe.description} \n " +
        f"No. Servings: {_recipe.no_servings} \n " +
        f"Callories per portion: {_recipe.calories_per_portion} \n"
    )
    print("Ingredients:")
    for _ingredient in _recipe.ingredients:
        print(_ingredient.pretty_format())
    print("\nInstructions:")
    for instruction in _recipe.instructions:
        print(f"\n{instruction}")


apple_pie_recipe = recipe.Recipe(title="Apple Pie")
apple_pie_recipe.description = "Simple Traditional Apple Pie Recipe"
apple_pie_recipe.no_servings = 12
apple_pie_recipe.calories_per_portion = 250
apple_pie_ingredients = [
    ingredient.Ingredient("Apple", 12.0, "Each", ["Apples"], 1136),
    ingredient.Ingredient(
        "Plain Flour", 1000.0, "grammes", ["Wheat", "Cereals", "Gluten"], 2090
    ),
    ingredient.Ingredient("Butter", 1400.0, "grammes", ["Dairy"], 10360),
    ingredient.Ingredient("Honey", 8.0, "tbsp", ["Honey"], 512),
    ingredient.Ingredient("Cinnamon", 4, "Pinch", [], 3),
    ingredient.Ingredient("Mixed Spice", 4, "Pinch", [], 3),
    ingredient.Ingredient("Beaten Egg", 4, "Each", ["Egg"], 360),
]

apple_pie_recipe.ingredients = apple_pie_ingredients

apple_pie_recipe.instructions = [
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

# Print out the recipe
pretty_print_recipe(apple_pie_recipe)

# Add some custard to ingredients list
apple_pie_recipe.add_ingredients(
    [ingredient.Ingredient("Custard", 200, "ml", ["Egg", "Milk"], 600)]
)

# Add instruction to serve with custard
new_instruction = apple_pie_recipe.instructions + [
    "STEP 7 - Serve with custard and enjoy!"
]

# Set the new list of instructions in the recipe instance
apple_pie_recipe.instructions = new_instruction

# Print the new recipe
pretty_print_recipe(apple_pie_recipe)

# Oh no if people are on a diet this might not be so wise

print("\n****I'm on a diet no custard for me I might get tempted!****\n")

# Remove ingredient from list
apple_pie_recipe.remove_ingredient(
    ingredient.Ingredient("Custard", 200, "ml", ["Egg", "Milk"], 600)
)

# Remove the step from the instructions
apple_pie_recipe.remove_instruction("STEP 7 - Serve with custard and enjoy!")

# Print the updated recipe
pretty_print_recipe(apple_pie_recipe)
