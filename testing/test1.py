# *********************************************
# Lesson 1: 
# 1. How to execute a python file
# 2. Explore built in functions
# 3. Explore simple arguments
# *********************************************


#
# this is a comment in a python script file
#

#
# How to execute a python file:
# c:\>python script-filename.py
#

#
# Python programs are text files
# It is a convention to use .py as its extension
#

#
# Built in functions
#

#print is a built-in function
print ("hello")
#see docs for other built-in functions

#
#Exploring arguments
#

# print "hello" 
# won't compile because no brackets around args

# print (hello) 
# won't compile because the symbol 'hello' is not known

print (str) 
# works, because 'str' is a known symbol, a class name

print ("hello1","hello2");
# function with 2 arguments

print ("hello3" "hello4");
# looks like 2 arguments, but it is actually one argument
# what is inside the brackets is a single argument 

x = "hello5"
print(x) # prints hello5

x = "hello6" "-hello7"
print (x) #hello6-hello7
#this is because of the nature of string initialization

x = "hello7", "hello8"
print(x)
# now x becomes a list
