pi = 3.14
def area_of_circle(r):
    return pi * r * r

r = int(input("Enter the radius of the circle: "))
area = area_of_circle(r)
print("The area of the circle with radius", r, "is: ", area)