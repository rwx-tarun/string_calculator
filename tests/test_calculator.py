from string_calculator.calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_value():
    assert add("1") == 1


def test_two_numbers_return_sum():
    assert add("1,5") == 6


def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_multiple_negatives_in_exception_message():
    with pytest.raises(ValueError, match="negative numbers not allowed"):
        add("1,-1,2,-3")
