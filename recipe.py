#Recipe Class

class Recipe:


    def __init__(self, title):
        self.title = title
        self.description = None
        self.noServings = None
        self.caloriesPerPortion = None
        self.ingredients = []
        self.instructions = None

    def getDescription(self):
        return self.description
    
    def setDescription(self,description):
        self.description = description

# r1 = Recipe("Lasagne")
# r1.setDescription("Layers of pasta cheese and tomato sauce")
# print(r1.getDescription())






