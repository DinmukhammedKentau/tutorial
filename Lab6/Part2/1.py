import functools
numbers=[1,2,3,4,5,6]
productOfNumbers=functools.reduce(lambda x,y:x*y,numbers)
print(productOfNumbers)
"""пайтоннын 2 ши версиясында reduce дегенди тарту ушин 
functools шакырудын кажети жок тугын"""
"""numbers = [1, 2, 3, 4, 5]
prod = 1
for i in numbers:
    prod *= i
print(prod)"""
