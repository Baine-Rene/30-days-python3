# Day 5 - 30 day python challenge

empty_list = []

stationary = ['pens', 'markers', 'pencils', 'ruler', 'brush', 'ink']
print(len(stationary))

print(stationary[0])
print(stationary[3])
print(stationary[5])

mixed_data_types = ['Rene Baine', 22, {'height': 175, 'Marita_Status': 'Not Married', 'Address': '571 reid street'}]

companies = ['Apple', 'IBM', 'Oracle', 'Amazon', 'Google']

print(mixed_data_types)
print(companies)

print('The number of companies on the list is', len(companies))

companies[0] = 'Nvidia'

# Adding an element to the companies list
companies.append('Microsoft')

print(companies[0])
print(companies[2])
print(companies[4])

print(companies)

# Joining two lists

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

fullstack = front_end + back_end
print(fullstack)