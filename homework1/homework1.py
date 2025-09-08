# File: homework1 .py

#--- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # an integer is any whole number
b = 1.5
print(b)
print(type(b)) # a float is a number with decimals or fractions
c = 3j
print(c)
print(type(c)) # c is a complex number, a combination of real numbers and imaginary numbers
d = "hello"
print(d)
print(type(d)) # d is a string, a sequence of characters with no numbers
e = [1, 2, 3]
print(e)
print(type(e)) # e is a list, a colelction of integers
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f)) # f is a dictionary, a list that has words connected to their definition
g = (1, 2)
print(g)
print(type(g)) # g is a tuple, a immutable and ordered list of numbers
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h)) # h is a list, this is a list of strings
i = True
print(i)
print(type(i)) # i is a boolean, this is a datatype which is only true or false
j = None
print(j)
print(type(j)) # this is a nonetype, this represents a data with the abscence of a value
k = [True, "blue", 12]
print(k)
print(type(k)) # this is a list, this list is a combination of multiple other types
l = str(14)
print(l)
print(type(l)) # this is a string, specifically the string fuction converts other data types into a string
m = 1e4
print(m)
print(type(m)) # this is a float, a number which is not fully whole and include all otehr real numbers

#1. 9 unique datatypes
#2. string, integer, float, dict, list, complex, bool, nonetype, tuple
#3. b and m are both floats; e, h, and k  are both lists; d and l are both strings
#4. l was a string implying the string function takes whatever input and outputs a string 
n = range(5)
print(n)
print(type(n)) # this is a range, which is a n immutable sequence of numbers

#---Booleans---
print(10 > 9) #True, 10 is greater than 9
print(10 == 9) #False, 10 is not equal to 9
print(10 <= 9) #False, 10 is not less than or equal to 9
print(bool("abc")) #True, the boolean function returns true for any real input
print(bool(123)) #True, this has a value therefore it is true
print(bool(["apple", "cherry", "banana"])) #True, it is a datatype so the booolean outputs true
print(bool(True)) #True, the input says true so its true
print(bool(False)) #False, inout says false 
print(bool(0)) #False, no value for boolean to be true
print(bool("")) #False, This is an empty set
print(bool(" ")) #True, although nothign is there there is a blank string therefore true
print(bool(())) #False, empty set
print(bool([]))#False, empty set 
print(bool({})) #False empty set
print(bool(True and False)) #False, would only be true is the two conditions are the same
print(bool(True and True)) #True, both condintions are the same so true
print(bool(False and False)) #False, same as previous line
print(bool(True or False)) #True, the operator requires one true statement namely the true
print(bool(True or True)) #True, same as line above
print(bool(False or False)) #False, no true to make it true
print(bool(not(False))) #True, the boolean of not false which is true
print(bool(not(True))) #False,  same as above but flipped
# A pattern I noticed was the booleans with some sort of data resulted in true while empty sets resulted in false
# The one that surprised me the most was bbool(" ") because I expected to count as an empty set 
bool((1,2)) #this results true because there is a valid datatype inside the bool function
bool(None) #this is false because the boolean has no value to say is truew therefore it is false

#---Operators---
print(10+5) #15, + performs additoins
print(10-5) #5, - performs subtraction
print(2 * 4) #8, * performs multiplication
print(6 / 3) #2, / performs division
print(5 % 2) #1, % performs modulus, findging the remainder
print(3 ** 2) #9, ** performs exponentiation
print(15 // 2) #7, // performs floor division, divinding then rounding to the lower number
print(5==2) #False, == performs equals to 
print(10 != 10) #False, != performs does not equal
print(2<5) #True, < performs less than 
print(12>5) #True, > performs greater than
print(5<=6) #True, <= performs less then or equal to
print(1>=10) #False, >= performs greater than or equal to
x = 5
x += 5 # 10, += take the variable and adds the value to it
print(f"{x=}") 
x -= 4 #6, -= takes the value of the variable and substracts the value from it
print(f"{x=}")
x *= 3 #18, *= takes the variable and multiplies the value by it
print(f"{x=}")
#and returns true only if both inputs are true, True and True, True and False
#or returns true if one of the entries is true, True or False, False or False
#not reverses the result of the input, not(False), not(True)
#the difference between / and // is // will use the floor function after divinding 
#% is the modulus while // is floor division
#you would use % to find teh remainder, Ex. print(16 % 3) will return 1
#assingm,ent operators workl by taking the current value of the vraible and then performing the specified operation with the value 

#---Strigns---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints: h
print(my_string[1]) # Prints: e
print(my_string[2]) # Prints: l
print(my_string[3]) # prints: l
print(my_string[4]) # prints: o
print(my_string[-1]) # prints: o
print(my_string[1:3]) # prints: el
print(my_string[0:5:2]) # prints: hlo
print(len(my_string)) # prints 5
print( my_string + "goodbye") # prints: hellogoodbye
print(7 * my_string) # pritns: hellohellohellohellohellohellohello
#slicing is when you take a string and only print certain parts of the string manipulations 2 - 9 were examples of slicing
name = "Oski"
print("Hello, my name is", name) # this printed the fist string in the print stement catanated with the name variable
print(f"Hello, my name is {name}") # this printed the string in the print statement with the variable in curly brackets repalced with teh value of the variable
#the difference between teh last 2 statements is teh second is an f-strign which allows you to directly embed variables into strigns rather than seprating elemnts by commas

#---Terminal Commands---
# cd
# changes directories. use it to moce folders in your computer
# Example: cd python_decal_fa25

# ls
# shows the contents of a directory
# Example: ls python_decal_25/Alex

# ls -a
# lists all files in directory including hidden ones
# Example: ls -a Users/Alex

# mkdir
# makes a new directory
# Example: mkdir homework2 

# cat
# used to show the contents of files in a firectory and can be used to combine multiple files into 1
# Example: cat File1

# pwd
# shows the full path of the current directory
# Example: pwd

# cd ..
# moves up one directory
# example: cd.. 

# cd .
# this returns the current directory 
# Example: cd .

# cd ~ 
# changes to the home directory
# Example: cd ~

# cp
# used to copy directories and/or files to another location
# example: cp /path/to/current_directory/file1.py /path/to/new_directory/copy_file1.py

# mv
# moves a file or directory to a new directory
# Example: mv file1.txt path/new/directory

# rm
# remove. removes a file or directory
# Example: rm /path/to/directory/file1.txt

# clear
# used to clear the text on your terminal
# Example; clear

# grep
# global regular expression print. used to find recurring patterns in files
# Example: grep "pattern" homework1.py

# sort
# used to sort data within a file
# Example: sort my_file.txt

# zip
# used to archive files and directories
# Example: zip file1 file2

# kill
# used to terminate precesses in the terminal
# Example: kill [option] .. ..
# the difference between ls and ls -a is ls shows hidden files and directories
# a hidden file is a file not shown in the gui to prevent deletion or manipulation
# -n for cat, adds numbers to each line 
# - for cd, returns to the previous directory
# -r for rm, removes everythin inside a folder as well
