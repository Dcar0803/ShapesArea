from main import rectangle_area
def test_calculate_rectangle_area():
    assert rectangle_area(2,10) == 20
    assert rectangle_area(5,10) == 50
    assert rectangle_area(10,0) == 0

def  test_calculate_triangle_area():
    assert triangle_area(10 ,5) == 25.0
    assert triangle_area(0, 5) == 0
    assert triangle_area(3, 6) == 9.0