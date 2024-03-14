from src.models.ingredient import Restriction
from src.models.ingredient import Ingredient


truid = 'queijo'
nn = 'não é queijo'
larajinha = 'camarão'
compara = "Ingredient('queijo')"
# Req 1


def test_ingredient():
    cc = Ingredient(larajinha)
    oqrt = Ingredient(truid)
    qrt = Ingredient(truid)
    xxt = Ingredient(nn)
    assert qrt.__repr__() == compara
    assert qrt.__hash__() != xxt.__hash__()
    assert qrt.__eq__(oqrt) is True
    assert qrt.__hash__() == oqrt.__hash__()
    assert qrt.name == truid
    assert cc.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
    }
    assert qrt.__eq__(xxt) is False
