import sys
sys.path.append("../")
from ingredient import Ingredient

apple = Ingredient(name="Granny Smith", amount=1.0, units="each", alergens=[], callories=50.0)

print(apple.pretty_format())
