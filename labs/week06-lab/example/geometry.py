def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = 0.5 * base * height
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 1/2 x {height} × {base} = {area}")
    print()

print("Calculating triangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

