# Create a function calculate_area that accepts the radius of a circle as an argument and returns the area.
# Use the formula area=π×radius2\text{area} = \pi \times \text{radius}^2area=π×radius2 (Hint:
# You may use the math module to import the value of π).

import math
def circle(radius):
    area = math.pi * radius**2
    print(area)

circle(5) 