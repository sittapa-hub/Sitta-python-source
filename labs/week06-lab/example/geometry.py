def calculate_triangle_area(height, base):
    """Calculates and displays triangle area"""
    area = 0.5 * base * height
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 1/2 x {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)


 # จากตัวอย่าง ให้สร้าง function สำหรับคำนวณพท.วงกลม
def calculate_circle_area(radius):
    """Calculates and displays circle area"""
    area = 3.14 * radius ** 2
    print(f"Circle with radius {radius}")
    print(f"Area = 3.14 x {radius} x {radius} = {area}")
    print()

print("Calculating circle areas:")
calculate_circle_area(5)
calculate_circle_area(7)