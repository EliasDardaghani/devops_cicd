from shop_app.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(1, 1) == 2

def test_add_negative_ones():
    calculator = Calculator()
    assert calculator.add(-1, -1) == -2