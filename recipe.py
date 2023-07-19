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
    
    def set_no_servings(self, no_servings:int):
        self._no_servings = no_servings


    def get_calories_per_portion(self):
        return self._calories_per_portion
    
    def set_calories_per_portion(self, calories_per_portion:int):
        self._calories_per_portion = calories_per_portion
    
    def get_ingredients(self):
        return self._ingredients
    
    def set_ingredients(self,ingredients):
        self._ingredients.append(ingredients)
        if len(set(self._ingredients)) != len(self._ingredients):
            self.remove_ingredient(ingredients) #I have tested this and it only removes the recently added ingredient
            return False
    
    def remove_ingredient(self,ingredient):
        self._ingredients.remove(ingredient)
        #[x for x in self._ingredients if x is not None] #tried to use list comprehension to get rid of the none value in self._ingredients did not succeed
        #Do I need to prevent this removing duplicates if I have already prevented duplication with the set ingredients validation

    def display_ingredients(self):
        for ingredient in self._ingredients:
            print(ingredient) #When i use return it only returns the first value tomato I am not sure why
        #Not sure how to return this as a string
    
    def get_instructions(self):
        return self._instructions

    def set_instructions(self, instructions):
        self._instructions.append(instructions)
        
    def remove_instruction(self, instruction):
        self._instructions.remove(instruction)

    def pretty_format(self):
        return f"This is the recipe for {self._title}.\n{self._description}\nThe ingredients are: {self.display_ingredients()}"
        #Does not display ingredients correctly as display_ingredients doesn't work
    


