from testrecipemanager import TestRecipeManager
from pathlib import Path

testrecipemanager = TestRecipeManager(Path("./testdata"))

run = True

while run:
   run = testrecipemanager.menu()

print("Thank you for using recipe manager!")
