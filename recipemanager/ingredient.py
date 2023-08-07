"""
Ingredient class definition
"""


class Ingredient:
    """This class encapsulates what is in an ingredient as part of a recipe.
    it contains a name for the ingredient, the amount required,
    the units associated with the amount, a list of alergens that the
    ingredient might contain e.g. wheat and the number of callories
    associated with the amount.
    """

    def __init__(
        self,
        name: str,
        amount: float,
        units: str,
        alergens: list[str],
        callories: float,
    ):
        self._name_of_ingredient = name
        self._amount = amount
        self._units = units
        self._alergens = alergens
        self._callories = callories

    @property
    def name(self):
        """
        Getter for name of ingredient
        """
        return self._name_of_ingredient

    @property
    def amount(self):
        """
        Getter for amount of ingredient
        """
        return self._amount

    @property
    def units(self):
        """
        Getter for units of ingredient
        """
        return self._units

    @property
    def alergens(self):
        """
        Getter for alergens of ingredient
        """
        return self._alergens

    @property
    def callories(self):
        """
        Getter for callories of ingredient
        """
        return self._callories

    @amount.setter
    def amount(self, amount: float):
        """
        Setter for callories of ingredient
        """
        self._amount = amount

    @units.setter
    def units(self, units: str):
        """
        Setter for units of ingredient
        """
        self._units = units

    @alergens.setter
    def alergens(self, alergens: list[str]):
        """
        Setter for alergens of ingredient
        """
        self._alergens = alergens

    @callories.setter
    def callories(self, callories: float):
        """
        Setter for callories of ingredient
        """
        self._callories = callories

    def pretty_format(self) -> str:
        """
        Creates a pretty formated description of the ingredient
        """
        if len(self._alergens) > 0:
            alergen_list = ", ".join(self._alergens)
            return_string = str(
                f"{self._amount} {self._units} of {self._name_of_ingredient} "
                + f"containing {self._callories} callories "
                + f" - warning contains: {alergen_list}"
            )
        else:
            return_string = str(
                f"{self._amount} {self._units} of {self._name_of_ingredient} "
                + f"containing {self._callories} callories"
            )

        return return_string
