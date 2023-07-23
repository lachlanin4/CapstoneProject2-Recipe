from TestRecipeManager import TestRecipeManager
from pathlib import Path

testrecipemanager = TestRecipeManager(Path("./testdata"))

while True:
   testrecipemanager.menu()
