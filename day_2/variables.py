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


