# Day 3 - 30 day python challenge

age = 21
height = 175.00
complex_num = (1 + 1j)

base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")

area = 0.5 * int(base) * int(height)
print('The area of the triangle is: ',area)

# Calculating the perimeter of the triangle

side_a = input("Enter side a:")
side_b = input("Enter side b:")
side_c = input("Enter side c:")

perim = int(side_a) + int(side_b) + int(side_c)

print('The perimeter for the triangle is:', perim)

# Calculating the area and perimeter of a rectangle

length = input("Enter the base of the rectangle: ")
width = input("Enter the base of the rectangle: ")

area = int(length) * int(width)
perim_rec = 2 * (int(length) + int(width))

print('The area of the rectangle is: ',area)
print('The perimeter of the rectangle is:', perim_rec)

