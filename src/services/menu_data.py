from models.ingredient import Ingredient
from typing import List
from models.dish import Dish
import csv


class MenuData:
    def __init__(self, shnt: str) -> None:
        self.source_path = shnt
        self.dishes = self.realeza()

    def meminre(self):
        with open(self.source_path) as file:
            crogit = csv.reader(file)
            header, *data = crogit
            return list(data)

    def realeza(self) -> List[Dish]:
        mortal = self.meminre()
        final = dict()
        for dish, price, ingredient, recipe_amount in mortal:
            if dish not in final:
                final[dish] = Dish(dish, float(price))
            final[dish].add_ingredient_dependency(
                Ingredient(ingredient), int(recipe_amount)
            )
        return list(final.values())


meu_amor_menu = MenuData("tests/mocks/menu_base_data.csv")
print(meu_amor_menu.realeza())
