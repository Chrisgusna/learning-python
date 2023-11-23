def calculate_square_area(side: float):
    return side * side 


def calculate_rectangle_area(length: float, width: float):
    return length * width


def calculate_circle_area(radius: float):
    pi = 3.14
    return pi * radius ** 2

def calculate_rhombus_area(p:float, q:float):
    return (p * q) / 2 

print("""
---------------
Area calculator
---------------
Select a shape:
""")

selection = input ("""\t'S' - Square
\t'R' - Rectangle
\t'C' Circle
\t'RM' Rhombus
""")

area = 0

if selection == 'RM':
    p = input("Enter the p: ")
    q = input ("Enter the q: ")
    area = calculate_rhombus_area(float(p), float(q))

def get_shape_name(tag):
    if tag == 'RM':
        shape = 'Rhombus'

print(f"The area of the {get_shape_name(selection)} is {area}")