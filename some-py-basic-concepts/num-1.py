# #type casting ✅✅✅
# a='1'
# b=2
# print(int(a)+b) #3

# #string indexing ✅✅✅
name='harry'
# print(name[0]) #h

# #string slicing ✅✅✅
# print(name[0:3]) #har
# print(name[0:]) #harry
# print(name[0:4:2]) #hr  #step argument
# print(name[::-1]) #yrrah  #reverse string

#string methods ✅✅✅
# website='http://google.com'
# print(website.replace('http://','https://')) #https://google.com
# slice=slice(8,-4)
# print(website[slice]) #google

# #string methods ✅✅✅
# name='harry'
# print(name.upper()) #HARRY
# print(name.lower()) #harry
# print(name.title()) #Harry
# print(name.count('h')) #2

# #string formating ✅✅✅
# name='harry'
# print(f'hello {name}') #hello harry


#math module ✅✅✅
# import math
# print(math.sqrt(16)) #4
# print(math.pow(2,3)) #8
# print(math.pi) #3.141592653589793
# print(math.e) #2.718281828459045
# print(math.ceil(1.2)) #2
# print(math.floor(1.2)) #1
# print(math.factorial(3)) #6
#print(dir(math))#['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']



#built-in function in Python.✅✅✅
#print(round(1.2)) #1
#print(abs(-1)) #1
#print(len('hello')) #5
#print(len((1,2,3,4,5))) #5
#print(len({'a':1,'b':2,'c':3})) #3
#print(len({'a','b','c'})) #3
# print(max(1,2,3,4,5)) #5
#print(min(1,2,3,4,5)) #1
# print(pow(2,3)) #8
#print(sqrt(16)) #4
#print(sin(1)) #0.8414709848078965
#print(cos(1)) #0.5403023058681398
#print(tan(1)) #1.5574077246549023


#if else statement ✅✅✅
# age=int(input('enter your age: '))
# if age>=18:
#     print('you are an adult')
# elif age>=13:
#     print('you are a teenager')
# else:
#     print('you are a child')

#logical operators ✅✅✅
# and
# or
# not

#and operator ✅✅✅
# print(True and True) #True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False
#or operator ✅✅✅
# print(True or True) #True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False
#not operator ✅✅✅
# print(not True) #False
# print(not False) #True

#while loop ✅✅✅
# i=0
# while i<10:
#     print(i)
#     i+=1

#for loop ✅✅✅
# for i in range(10):
#     print(i)

#for loop ✅✅✅
# for i in range(5,100,2): #52,54,56
#     print(i)

#for loop ✅✅✅
# for second in range(10,0,-1): #10,9,8,7,6,5,4,3,2,1
#     print(second)

#break statement ✅✅✅
# for i in range(10):
#     print(i)
#     if i==5:
#         break

#nested loop ✅✅✅
# for i in range(10):
#     for j in range(10):
#         print(i,j)

#list ✅✅✅
# fruits=['apple','banana','cherry']
# print(fruits) #['apple','banana','cherry']
# print(fruits[0]) #apple
# print(fruits[1]) #banana
# print(fruits[2]) #cherry

#list methods ✅✅✅
# fruits=['apple','banana','cherry']
# fruits.append('orange')
# print(fruits) #['apple','banana','cherry','orange']
# fruits.remove('banana')
# print(fruits) #['apple','cherry','orange']
# fruits.pop()
# print(fruits) #['apple','cherry'] #remove last element
# fruits.pop(1)
# print(fruits) #['apple','cherry'] #remove element at index 1
# fruits.insert(1,'orange')
# print(fruits) #['apple','orange','cherry'] #insert element at index 1
# fruits.sort()
# print(fruits) #['apple','banana','cherry'] #sort list
# fruits.reverse()
# print(fruits) #['cherry','banana','apple'] #reverse list
# fruits.clear()
# print(fruits) #[] #clear list
# fruits.copy()
# print(fruits) #['apple','banana','cherry'] #copy list
# fruits.count('apple')
# print(fruits) #1 #count element in list
# fruits.index('apple')
# print(fruits) #0 #index of element in list
# fruits.extend(['orange','mango'])
# print(fruits) #['apple','banana','cherry','orange','mango'] #extend list

#2d list ✅✅✅
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix) #[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0]) #[1,2,3]
# print(matrix[0][0]) #1
# print(matrix[1][2]) #6
# print(matrix[2][1]) #8

#tuple ✅✅✅ cannot be modified
# fruits=('apple','banana','cherry')
# print(fruits) #('apple','banana','cherry')
# print(fruits[0]) #apple
# print(fruits[1]) #banana
# print(fruits[2]) #cherry

#tuple methods ✅✅✅
# fruits=('apple','banana','cherry')
# print(fruits.count('apple')) #1
# print(fruits.index('banana')) #1


#set ✅✅✅  unordered and unindexed it does not allow duplicate values
# fruits={'apple','banana','cherry'}
# print(fruits) #{'apple','banana','cherry'}
# fruits.add('orange')
# print(fruits) #{'apple','banana','cherry','orange'}
# fruits.remove('banana')
# print(fruits) #{'apple','cherry','orange'}

#set methods ✅✅✅
# fruits={'apple','banana','cherry'}
# print(fruits) #{'apple','banana','cherry'}
# fruits.add('orange') #add element to set
# print(fruits) #{'apple','banana','cherry','orange'}
# fruits.remove('banana') #remove element from set
# print(fruits) #{'apple','cherry','orange'}
# fruits.clear() #clear set
# print(fruits) #{'apple','banana','cherry'}
# fruits.pop()
# print(fruits) #{'apple','banana','cherry'}
# fruits.copy() #copy of set
# print(fruits) #{'apple','banana','cherry'}
# fruits.union({'orange','mango'}) #union of two sets
# print(fruits) #{'apple','banana','cherry','orange','mango'}
# fruits.intersection({'apple','banana','cherry'}) #intersection of two sets
# print(fruits) #{'apple','banana','cherry'}
# fruits.difference({'apple','banana','cherry'}) #difference of two sets
# print(fruits) #{'apple','banana','cherry'}
# fruits.symmetric_difference({'apple','banana','cherry'}) #symmetric difference of two sets
# print(fruits) #{'apple','banana','cherry'}





