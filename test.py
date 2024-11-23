from main import rectangle_area, triangle_area
import pytest

def test_calculate_rectangle_area():
    assert rectangle_area(2,10) == 20
    assert rectangle_area(5,10) == 50
    assert rectangle_area(10,0) == 0

def  test_calculate_triangle_area():
    assert triangle_area(10 ,5) == 25.0
    assert triangle_area(0, 5) == 0
    assert triangle_area(3, 6) == 9.0

def test_calculate_circle_area():
    assert circle_area(7) == pytest.approx(153.938, rel=1e-3)
    assert circle_area(0) == 0
    assert circle_area(1) == pytest.approx(3.14159, rel=1e-5)