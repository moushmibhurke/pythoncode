def calculate_area(base,height,type):
    total=0
    if type=="triangle":
       total= 1/2*(base*height)
       return total
    elif type=="rectangle":
        total=base*height
        return total
    else:
        print("invalid entry")

triangle_base=input("please enter value for base:")
triangle_base=float(triangle_base)
triangle_height=input("please enter value for height:")
triangle_height=float(triangle_height)
type=input("please enter type:")
area=calculate_area(triangle_base,triangle_height,type)
print("area of",type,"is",area)