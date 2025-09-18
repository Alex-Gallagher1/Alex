# File: Homework3.py

#---Print Functions---
def say_goodbye(name):
    print("goodbye,", name)

def area_circle(r):
    # prints the area of a circle for a given radius r
    pi = 3.14 
    print(pi*(r)**2)

#---Return Functions---
def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

#---Conditionals---
def temperature(list):
    return (min(list), max(list))  

def weekend(number):
    if number == 6 or number == 7:
        return "It's the Weekend"
    elif number > 7: #This section is to cap the function for integers greater than 7
        return None
    else:
        return "It's not the Weekend"

def fuel_eff(miles, used_fuel):
    return miles/used_fuel # output would be in units of miles per gallon

def encryption(integer):
    last_digit = integer % 10
    new_integer = integer // 10
    n = len(str(new_integer)) 
    return new_integer + last_digit*10**n

#---Loops---
def power(x,y):
    result = 1
    for i in range(0,y):
        result *= x
    return result


mylist = [0, 1, -2, 15, 30]
def min1(mylist):
    minimum = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] < minimum:
            minimum = mylist[i]
    return(minimum) 

def max1(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return(max)

def min2(list):
    min = list[0]
    index = 0
    while index < len(list):
        if list[index] < min:
           min = list[index]
        index += 1
    return(min)

def max2(list):
    max = list[0]
    index = 0
    while index < len(list):
        if list[index] > max:
            max = list[index]
        index += 1
    return(max)

def sum_int(integer):
    sum_digits = 0
    while integer != 0:
        digit = integer % 10
        sum_digits = sum_digits + digit 
        integer = integer // 10
    return(sum_digits)

integer = 314159265359
result = sum_int(integer) # will add the digits in the integer containign the digits of pi

# print(f'The sum of the first 12 digits of pi is {result}')
#print(subtract(6,7))