# Ingredient class definition
class Ingredient:
    """This class encapsulates what is in an ingredient as part of a recipe.
    it contains a name for the ingredient, the amount required, the units associated with the amount,
    a list of alergens that the ingredient might contain e.g. wheat and the number of callories
    associated with the amount."""

    def __init__(
        self, name: str, amount: float, units: str, alergens: [str], callories: float
    ):
        self._name_of_ingredient = name
        self._amount = amount
        self._units = units
        self._alergens = alergens
        self._callories = callories

    @property
    def name(self):
        return self._name_of_ingredient

    @property
    def amount(self):
        return self._amount

    @property
    def units(self):
        return self._units

    @property
    def alergens(self):
        return self._alergens

    @property
    def callories(self):
        return self._callories

    @amount.setter
    def amount(self, amount: float):
        self._amount = amount

    @units.setter
    def units(self, units: str):
        self._units = units

    @alergens.setter
    def alergens(self, alergens: []):
        self._alergens = alergens
