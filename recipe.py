from ingredient import Ingredient
from typing import List

# Recipe Class
class Recipe:
    def __init__(
        self,
        title,
        description=None,
        no_servings=None,
        calories_per_portion=None,
        ingredients=[Ingredient],
        instructions=[str],
        preperation_time=None,
    ):
        self._title = title
        self._description = description
        self._no_servings = no_servings
        self._calories_per_portion = calories_per_portion
        self._ingredients: List[Ingredient] = ingredients
        self._instructions: List[str] = instructions
        self._preperation_time = preperation_time

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def preperation_time(self):
        return self._preperation_time

    @preperation_time.setter
    def preperation_time(self, preperation_time):
        self._preperation_time = preperation_time

    @property
    def no_servings(self):
        return self._no_servings

    @no_servings.setter
    def no_servings(self, no_servings: int):
        self._no_servings = no_servings

    @property
    def calories_per_portion(self):
        return self._calories_per_portion

    @calories_per_portion.setter
    def calories_per_portion(self, calories_per_portion: int):
        self._calories_per_portion = calories_per_portion

    @property
    def ingredients(self) -> [Ingredient]:
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[Ingredient]):
        self._ingredients = ingredients

    # Method to progressively extend ingredients list
    def add_ingredients(self, ingredients: list[Ingredient]):
        if len(self._ingredients) > 0:
            self._ingredients.extend(ingredients)
        else:
            self._ingredients = ingredients

    # Method to progressively remove ingredients from list
    def remove_ingredient(self, ingredient: Ingredient):
        found = False
        for x, rec in enumerate(self._ingredients):
            if rec.name == ingredient.name:
                del self._ingredients[x]
                found = True
                break

        if not found:
            raise ("I couldn't find the recipe")

    @property
    def instructions(self):
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: list[str]):
        self._instructions = instructions

    # Method to progressively remove ingredients from list
    def remove_instruction(self, instruction):
        self._instructions.remove(instruction)
