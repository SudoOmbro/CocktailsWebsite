from typing import List, Union


class Ingredient:

    def __init__(
            self,
            name: str,
            link: str
    ):
        self.name: str = name
        self.link = link


class RecipeStep:

    def __init__(
            self,
            ingredient: Union[None, Ingredient],
            amount: float,
            description: Union[None, str]
    ):
        self.ingredient: Union[None, Ingredient] = ingredient
        self.amount: float = amount
        self.description: Union[None, str] = description

    def __repr__(self):
        if self.description:
            return self.get_description()
        if self.ingredient:
            return f"{self.ingredient.name} - {self.get_amount_string()}"
        return "???"

    def get_description(self) -> str:
        if self.ingredient:
            if self.description:
                return self.description.replace("[0]", self.ingredient.name).replace("[1]", self.get_amount_string())
            return f"{self.ingredient.name} | {self.get_amount_string()}"
        return self.description

    def get_amount_string(self) -> str:
        return f"{self.amount:.2f} Oz ({self.amount * 30:.2f} ml)"


class Cocktail:

    def __init__(
            self,
            cocktail_id: int,
            name: str,
            description: str,
            strength: int,
            recipe: List[RecipeStep]
    ):
        self.id: int = cocktail_id
        self.name: str = name
        self.description: str = description
        self.strength: int = strength
        self.recipe: List[RecipeStep] = recipe


class CocktailsFilter:

    def __init__(
            self,
            name: Union[str, None],
            strength: Union[int, None],
            ingredients: List[str]
    ):
        self.name = name,
        self.strength = strength
        self.ingredients = ingredients

