from recipemanager import RecipeManager
from recipemanager import Recipe

def main():
    recipe_manager = RecipeManager()



    while True:
        recipe_manager.menu()
        user_choice = input("Do you want to continue? (yes/no): ")
        if user_choice.lower() != "yes":
            print("Goodbye!")
            break

recipe_manager = RecipeManager()
main()