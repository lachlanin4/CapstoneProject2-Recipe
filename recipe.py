from ingredient import Ingredient

#Recipe Class
class Recipe:


    def __init__(self, title):
        self._title = title
        self._description = None
        self._no_servings = None
        self._calories_per_portion = None
        self._ingredients = list[Ingredient]
        self._instructions = list[str]

    def get_description(self):
        return self._description
    
    def set_description(self,description):
        self._description = description

    def get_no_servings(self):
        return self._no_servings
    
    def set_no_servings(self, no_servings:int):
        self._no_servings = no_servings


    def get_calories_per_portion(self):
        return self._calories_per_portion
    
    def set_calories_per_portion(self, calories_per_portion:int):
        self._calories_per_portion = calories_per_portion
    
    def get_ingredients(self) -> [Ingredient]:
        return self._ingredients
    
    def set_ingredients(self,ingredients:list[Ingredient]):
        self._ingredients = ingredients

    def add_ingredients(self,ingredients:list[Ingredient]):
        if len(self._ingredients) > 0:
           self._ingredients.extend(ingredients)
        else:
           self._ingredients = ingredients
    
    def remove_ingredient(self,ingredient:Ingredient):
        found = False
        for x, rec in enumerate(self._ingredients):
          if rec.name == ingredient.name:
            del self._ingredients[x]
            found = True
            break

        if not found:
          raise("I couldn't find the recipe")

    
    def get_instructions(self):
        return self._instructions

    def set_instructions(self, instructions:list[str]):
        self._instructions = instructions
        
    def remove_instruction(self, instruction):
        self._instructions.remove(instruction)
    


