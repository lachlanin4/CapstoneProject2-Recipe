"""
Recipe Class encapsulates everything required for a recipe
"""

from typing import List
from ingredient import Ingredient

# Recipe Class
class Recipe:
    """
    This is the initialisation for the recipe class
    """

    def __init__(
        self,
        title,
        description=None,
        no_servings=None,
        calories_per_portion=None,
        ingredients=None,
        instructions=None,
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
        """
        This is the getter for the Recipe title.
        """
        return self._title

    @property
    def description(self):
        """
        This is the getter for the Recipe description
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        This is the setter for the Recipe description
        """
        self._description = description

    @property
    def preperation_time(self):
        """
        This is the getter for the preperation time
        """
        return self._preperation_time

    @preperation_time.setter
    def preperation_time(self, preperation_time):
        """
        This is the setter for the preperation time
        """
        self._preperation_time = preperation_time

    @property
    def no_servings(self):
        """
        This is the getter for the number of servings
        """
        return self._no_servings

    @no_servings.setter
    def no_servings(self, no_servings: int):
        """
        This is the setter for the number of servings
        """
        self._no_servings = no_servings

    @property
    def calories_per_portion(self):
        """
        This is the getter for the number of calories per portion
        """
        return self._calories_per_portion

    @calories_per_portion.setter
    def calories_per_portion(self, calories_per_portion: int):
        """
        This is the setter for the number of calories in the recipe per portion
        """
        self._calories_per_portion = calories_per_portion

    @property
    def ingredients(self) -> [Ingredient]:
        """
        This is the getter for the ingredients list
        """
        return self._ingredients

    @ingredients.setter
    def ingredients(self, ingredients: list[Ingredient]):
        """
        This is the setter for the ingredients list
        """
        self._ingredients = ingredients

    # Method to progressively extend ingredients list
    def add_ingredients(self, ingredients: list[Ingredient]):
        """
        This is a way of adding ingredients to a recipe
        """
        if self._ingredients is not None:
            self._ingredients.extend(ingredients)
        else:
            self._ingredients = ingredients

    # Method to progressively remove ingredients from list
    def remove_ingredient(self, ingredient: Ingredient):
        """
        This is a way of removing ingredients from a recipe
        """
        found = False
        for _x, rec in enumerate(self._ingredients):
            if rec.name == ingredient.name:
                del self._ingredients[_x]
                found = True
                break

        if not found:
            raise "I couldn't find the recipe"

    @property
    def instructions(self):
        """
        This is a getter for the instructions list
        """
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: list[str]):
        """
        This is the setter for the instructions list
        """
        self._instructions = instructions

    # Method to progressively remove ingredients from list
    def remove_instruction(self, instruction):
        """
        This is a way to remove instructions from the list
        """
        self._instructions.remove(instruction)
