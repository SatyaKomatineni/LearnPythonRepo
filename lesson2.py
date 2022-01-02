#*********************************************
# Lesson 2: 
# Quick look at global functions: type, len, isinstance, slice
#
# full list at: https://docs.python.org/3.7/library/functions.html
#
# Noteworthy:
#
# 1. Functions explore the types of arguments that are passd to them
# 2. for example len() function will reject if a variable is not sequence
# 3. slice is a spec that can be used as an input to slice a sequence like a string
#
#***********************************************

#******************************
# type()
#******************************
x = 10
t = type(x)

print (t)
# prints <class,  int>
# the type of "x" is an integer

print(type(t))
# prints <class, type>
# the type of variable "t" is "type", a built-in type

#******************************
# len()
#******************************
s = "ssss"
print(len(s))
# prints 4 as the length of the string

anInteger = 15
vlen = len(s) #ok

#len = len(anInteger) 
# generates an error as "anInteger" is not of type "sized"
# interesting type.

alist = 10,15,16
print(alist)
#prints that list as (10,15,16)
#Notice the brackets ( and )

print(len(alist))
#prints 3

print(type(alist))
#prints <class, tuple>
#The type of the list is called 'tuple'
#read later how lists are classified in Python
#tuple: is an immutable list

#******************************
# isinstnace(variable-name, type-name)
#******************************
s = "string"
print(type(s))
#print <class str>

print(isinstance(s,str))
#prints True
#so variable "s" is an instance of "str" class

#******************************
# slice(start, stop, gap)
#******************************
s = "123456789"
x = sliceSpec = slice(3,8)
print(x)
# just prints slice(3,8,none)

#you can use that slice spec to get a new sequence
#using the slice as an input argument
y = s[sliceSpec]
print(y)

#prints "45678"

#Print the slice of a string called "s"
print(s[slice(4,6)])
#prints "56"