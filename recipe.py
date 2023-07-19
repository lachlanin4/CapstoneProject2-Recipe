#Recipe Class
class Recipe:


    def __init__(self, title):
        self._title = title
        self._description = None
        self._no_servings = None
        self._calories_per_portion = None
        self._ingredients = []
        self._instructions = []

    def get_description(self):
        return self._description
    
    def set_description(self,description):
        self._description = description

    def get_no_servings(self):
        return self._no_servings
    
    def set_no_servings(self, no_servings):
        if int(no_servings):
            self._no_servings = no_servings
        else:
            print("Please input an integer")

    def get_calories_per_portion(self):
        return self._calories_per_portion
    
    def set_calories_per_portion(self, calories_per_portion):
        if int(calories_per_portion):
            self._calories_per_portion = calories_per_portion
        else:
            print("Please input an integer")
    
    def get_ingredients(self):
        return self._ingredients
    
    def set_ingredients(self,ingredients):
        self._ingredients.append(ingredients)

    def remove_ingredient(self,ingredient):
        self._ingredients.remove(ingredient)

    def display_ingredients(self):
        print(self.get_ingredients()) #return a pretty string instead

    def get_instructions(self):
        return self._instructions

    def set_instructions(self, instructions):
        self._instructions.append(instructions)
        
    def remove_instruction(self, instruction):
        self._instructions.remove(instruction)
        






