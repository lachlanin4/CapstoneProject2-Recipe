#Recipe Class

class Recipe:


    def __init__(self, title):
        self.title = title
        self.description = None
        self.no_servings = None
        self.calories_per_portion = None
        self.ingredients = []
        self.instructions = None

    def get_description(self):
        return self.description
    
    def set_description(self,description):
        self.description = description

    def get_no_servings(self):
        return self.noServings
    
    def set_no_servings(self, no_servings):
        if int(no_servings):
            self.no_servings = no_servings
            print("This is an integer")
        else:
            print("Please input an integer")


r1 = Recipe("Lasagne")
# r1.set_description("Layers of pasta cheese and tomato sauce")
# print(r1.get_description())
#r1.set_no_servings(5)
 




