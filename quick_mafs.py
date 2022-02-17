import math

def area_of_house(length, width):
    house_area = length*width
    print(f"{house_area}sq.ft")
    return house_area

def area_of_circle(radius):
    circle_area = round(math.pi*(radius**2),3)
    return circle_area
    