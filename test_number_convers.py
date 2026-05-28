import pytest
import number_convers


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "10"),
        (3, "11"),
        (55, "110111"),
        (66, "1000010"),
        (77, "1001101"),
    ],
)
def test_natural_number_conversion(number, expected):
    result = number_convers.convert_natural_number(number)
    assert result == expected


def test_natural_number_conversion_for_negative_number():
    with pytest.raises(ValueError):
        number_convers.convert_natural_number(-1)

    with pytest.raises(ValueError):
        number_convers.convert_natural_number(-20)


def test_natural_number_conversion_raises_for_number_higher_than_16_bits():
    with pytest.raises(ValueError):
        number_convers.convert_natural_number(65536)
    with pytest.raises(ValueError):
        number_convers.convert_natural_number(-65537)


@pytest.mark.parametrize(
    "number, expected",
    [
        (-1, False),
        (0, True),
        (1, True),
        (2, True),
        (3, True),
        (55, True),
        (66, True),
        (3.5, False),
        ("1", False),
        (None, False),
    ],
)
def test_is_natual_number(number, expected):
    result = number_convers.is_natural_number(number)
    assert result == expected
