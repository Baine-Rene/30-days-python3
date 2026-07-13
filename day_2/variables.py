# Day 1 - 30 day python challenge

first_name = 'Rene'
last_name = 'Baine'
full_name = 'Rene Baine'
country = 'Uganda'
city = 'Kampala'
age = '21'
year = '2026'
is_married = 'No'
is_true = False
is_light_on = False
x, y, z = "apple", "banana", "orange"

# Checking variable types

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(x))
print(type(y))
print(type(z))

# Using the len() function
print(len(first_name))

# Comparing first and last name lengths 
if len(first_name) > len(last_name):
    print('First name is longer than last name')
elif len(first_name) < len(last_name):
    print('Last name is longer than first name')
else:
    print('First name and last name are of equal length')

# Declaring variable numbers and performing basic arithmetic

num_one = 5
num_two = 4

total = num_one + num_two 
diff = num_two - num_one
product = num_one * num_two
division = num_one/num_two
remainder = num_one%num_two
exp = num_one ** num_two
floor_division = num_one//num_two


print(total)
print(diff)
print(product)
print(division)
print(remainder)
print(exp)
print(floor_division)

# Calculating area and circumference of a circle

radius = 30

area_of_circle = 3.14159 * radius ** 2
circum_of_circle = 2 * (3.14159) * radius


print(area_of_circle)