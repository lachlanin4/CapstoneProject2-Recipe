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

    def getNoServings(self):
        return self.noServings
    
    def setNoServings(self, noServings):
        if int(noServings):
            self.noServings = noServings
            print("This is an integer")
        else:
            print("Please input an integer")


r1 = Recipe("Lasagne")
# r1.setDescription("Layers of pasta cheese and tomato sauce")
# print(r1.getDescription())
r1.setNoServings(5)
 




