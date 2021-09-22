def calculate_area(base,height):
    total=0
    total= 1/2*(base*height)
    return total

triangle_base=input("please enter value for base:")
triangle_base=float(triangle_base)
triangle_height=input("please enter value for height:")
triangle_height=float(triangle_height)
area=calculate_area(triangle_base,triangle_height)
print("area of triangle is:",area)
