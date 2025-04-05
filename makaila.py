#Function 1
# Returns Area of Rectangle-Makaila's functipn
def rect_area(length, width):
    return length * width

#Function 2
# Returns Surface Area of Rectangular Solid
def rect_surface_area(length, width, height):
    side1 = rect_area(length, width)
    side2 = rect_area(length, height)
    side3 = rect_area(width, height)
    return 2 * (side1 + side2 + side3)

#main program and request the dimension of a solid rectangular object-makaila's main program below
def main():
    length = int(input("Enter the length of the the object as a integer: "))
    width = int(input("Enter the width of the the object as a integer: "))
    height = int(input("Enter the height of the the object as a integer: "))
#computing surface area
    surface_area = rect_surface_area(length, width, height)

# Printing values
    print(f"Length = {length}, Width = {width}, Height = {height}")
    print(f"Total Surface Area = {surface_area}")
    print(f"Area of the rectangle = {rect_area(length, width)}")

#calling function
if __name__ == "__main__":
    main()
