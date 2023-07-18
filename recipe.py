#Recipe Class

class Recipe:


    def __init__(self, title):
        self.title = title
        self.description = None
        self.no_servings = None
        self.calories_per_portion = None
        self.ingredients = []
        self.instructions = [] #List or string data type?

    def get_description(self):
        return self.description
    
    def set_description(self,description):
        self.description = description

    def get_no_servings(self):
        return self.noServings
    
    def set_no_servings(self, no_servings):
        if int(no_servings):
            self.no_servings = no_servings
            #print("This is an integer")
        else:
            print("Please input an integer")

    def get_calories_per_portion(self):
        return self.calories_per_portion
    
    def set_calories_per_portion(self, calories_per_portion):
        if int(calories_per_portion):
            self.calories_per_portion = calories_per_portion
        else:
            print("Please input an integer")
    
    def get_ingredients(self):
        return self.ingredients
    
    def set_ingredients(self,ingredients):
        self.ingredients.append(ingredients)

    def get_instructions(self):
        return self.instructions

    def set_instructions(self, instructions):
        self.instructions.append(instructions)
        
        




r1 = Recipe("Lasagne")
# r1.set_description("Layers of pasta cheese and tomato sauce")
# print(r1.get_description())
#r1.set_no_servings(5)
# r1.set_ingredients("tomato")
# r1.set_ingredients("tomato")
# print(r1.get_ingredients())

 



