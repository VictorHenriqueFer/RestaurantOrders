from typing import Dict, List
from services.inventory_control import InventoryMapping
from services.menu_data import MenuData


DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, vr: str) -> None:
        try:
            curr_dish = [
                vhrtu
                for vhrtu in self.menu_data.dishes
                if vhrtu.name == vr
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")
        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        return [
            {
                "restrictions": vhrtu.get_restrictions(),
                "price": vhrtu.price,
                "ingredients": vhrtu.get_ingredients(),
                "dish_name": vhrtu.name,
            }
            for vhrtu in self.menu_data.dishes
            if restriction not in vhrtu.get_restrictions()
            and self.inventory.check_recipe_availability(vhrtu.recipe)
        ]
