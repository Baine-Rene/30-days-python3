# Day 4 - 30 day python challenge

space = ' '
title = 'Thirty' + space + 'Days' + space + 'of' + space + 'Python'
print(title)

coding = ['Coding', 'for', 'all']
result = ' '.join(coding)
print(result)

company = result
print(len(company))

capital = company.upper()
print(capital)

lower = company.lower()
print(lower)

capitalize = company.capitalize()
print(capitalize)

title = company.title()
print(title)

swap = company.swapcase()
print(swap)

compnay_slice = company[0:1]
print(compnay_slice)

substring = 'Coding'
print(company.rindex(substring))

print(company.replace('Coding', 'Python'))

title = ['Python', 'for', 'Everyone']
title_result = ' '.join(title)
print(title_result)

print(title_result.replace('Everyone', 'All'))