import sys

sys.path.append("../")
from ingredient import Ingredient

apple = Ingredient(
    name="Granny Smith", amount=1.0, units="each", alergens=[], callories=50.0
)

print(apple.pretty_format())

bread = Ingredient(
    name="White Bread",
    amount=1.0,
    units="slice",
    alergens=["Wheat", "Nuts"],
    callories=40.0,
)

print(bread.pretty_format())
