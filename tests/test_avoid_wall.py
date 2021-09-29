from server_logic import avoid_wall
import pytest


@pytest.mark.parametrize(
    "expected, body, hight, width",
    (
        ({"right", "left", "down", "up"}, [{"x": 3, "y": 3}], 20, 20),
        ({"right", "left", "down"}, [{"x": 3, "y": 20}], 20, 20),
        ({"right", "left", "up"}, [{"x": 1, "y": 0}], 20, 20),
        ({"right", "left", "up"}, [{"x": 1, "y": 0}], 20, 20),
        ({"right", "up"}, [{"x": 0, "y": 0}], 20, 20),
        ({"left", "down"}, [{"x": 20, "y": 20}], 20, 20),
    ),
)
def test_avoid_wall(expected, body, hight, width):
    result = avoid_wall(body, {"right", "left", "down", "up"}, hight, width)
    assert (
        result == expected
    ), f'avoid_wall({body=}, {{"right", "left", "down", "up"}}, {hight=}, {width=})'
