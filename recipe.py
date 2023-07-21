# Create a noddy form of recipe class
class Recipe:
   def __init__(self, name, instructions, ingredients):
      self._name = name
      self._instructions = instructions
      self._ingredients = ingredients

   @property
   def name(self):
      return self._name

   @property
   def instructions(self):
      return self._instructions

   @property
   def ingredients(self):
      return self._ingredients

   def pretty_description(self):
      pretty_str = str(f"{self._name}, instructions are {self._instructions} using {self._ingredients}")
      return pretty_str
      
