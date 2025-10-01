#File: homework4.py


#---3 Lists---
#--3.1 List Operatiosn--
favorite_foods = ["Pasta", "chicken", "rice", "poke", "sandwich"]

# print(favorite_foods[1])
# print(favorite_foods[-1])
favorite_foods.append("steak")
favorite_foods.insert(1, "apple") #Error:'str' object cannot be interpreted as an integer, forgot order so swapped the indexes inside the insert function
favorite_foods.remove("rice")
# print(len(favorite_foods))

# for food in favorite_foods:
    # print(food.upper())

new_list = favorite_foods[0::5]
# print(new_list)

def potato(favorite_foods):
    if "potato" in favorite_foods:
        print("A Potato!")
    else:
        print("No Potato")
 
# potato(favorite_foods)

#--3.2 Slicing and Striding--
numbers = list(range(21))

def get_first_15(list):
    return list[:16]

def get_every_5th(list):
    return list[::5]

def reverse_and_stride(list):
    new_list = list[::-1]
    return new_list[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)

#--3.3 Nested Lists--
numbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(numbers[2])
# print(numbers[1][1])

def sum_nested(nested_list):
    count = 0
    for list in nested_list:
        for entry in list:
            count += entry
    return count
# print(sum_nested(numbers))

#--3.4 Create a 5x5 List--
def fivebyfive(number):
    nested_list = []
    list = []
    for i in range(1,number+1):
        list.append(i)
        for j in list:
            if j % 5 == 0:
                new_list = list[:j]
                list = list[j:]
                nested_list.append(new_list)
    return nested_list

matrix = fivebyfive(25)
# print(matrix)

def multiples_of_three(nested_list):
    for list in nested_list:
        for i in range(len(list)):
            if list[i] % 3 == 0:
                list[i] = "?"
    return nested_list
"""kept running into issues with the syntax for the list becasue I was using the statement for i in list rather than for i in range(len(list))"""

def addfivebyfive(nested_list):
    count = 0
    for list in nested_list:
        for i in range(len(list)):
            if list[i] != '?':
                count += list[i]
            else:
                continue
    return count


threes = multiples_of_three(matrix)

sum_of_threes = addfivebyfive(threes)

#---4 Dictionaries---
#--4.1 Dictionary Operations--
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
# print(ages["Katie"]) 
"""Error: 'katie' I forgot to capitalize katie therefore the strigns didnt match for python so there was in error in the indexing"""
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

# for i in ages.items():
#     print(i)
"""Error: 'builtin_function_or_method' object is not iterable, forgot the empty parenthesis for the values function, added them and code worked """
        
#---Running Your Code---
test_code = fivebyfive(100)
# print(test_code)
