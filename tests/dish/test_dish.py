import pytest
from src.models.dish import Dish
from src.models.ingredient import Restriction
from src.models.ingredient import Ingredient


craq = "queijo gorgonzola"
final = "Dish('pastel', R$45.00)"
gil = 'macarrão com queijo'
dr = "pastel"
fd = '11234'


def test_dish():
    pp = Dish('pastel', 45)
    xxt = Dish(gil, 45)
    mbt = Dish(gil, 45)
    assert xxt.__eq__(pp) is False
    assert pp.__repr__() == final
    assert xxt.name == gil
    assert (xxt.__hash__()
            == mbt.__hash__())
    assert xxt.__eq__(mbt) is True
    assert xxt.__hash__() != pp.__hash__()
    with pytest.raises(ValueError):
        Dish(dr, -45)
    with pytest.raises(TypeError):
        Dish(dr, fd)
    xxt.add_ingredient_dependency(
        Ingredient(craq), 2
    )
    assert xxt.recipe.get(Ingredient(craq)) == 2
    assert xxt.get_restrictions() == {
        Restriction.ANIMAL_DERIVED, Restriction.LACTOSE
    }
    assert (xxt.get_ingredients()
            == {Ingredient(craq)})
