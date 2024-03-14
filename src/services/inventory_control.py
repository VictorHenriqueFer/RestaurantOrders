from csv import DictReader
from typing import Dict
from src.models.dish import Recipe
from src.models.ingredient import Ingredient


BER = "data/inventory_base_data.csv"
Inventory = Dict[Ingredient, int]


def read_csv_inventory(inventory_file_path=BER) -> Inventory:
    inventory = dict()
    with open(inventory_file_path, encoding="utf-8") as file:
        for row in DictReader(file):
            ingredient = Ingredient(row["ingredient"])
            inventory[ingredient] = int(row["initial_amount"])
    return inventory


class InventoryMapping:
    def __init__(self, inventory_file_path=BER) -> None:
        self.crude = read_csv_inventory(inventory_file_path)

    def check_recipe_availability(self, xique: Recipe) -> bool:
        return all(
            self.crude.get(ingredient, 0) >= quantity
            for ingredient, quantity in xique.items())

    def consume_recipe(self, xique: Recipe) -> None:
        pass
