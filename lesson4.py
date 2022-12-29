#*********************************************
# Lesson 4: 
# Very basic string manipulation
#
# Strings: https://docs.python.org/3.7/library/string.html
# format examples: https://docs.python.org/3.7/library/string.html#format-examples
#
# Noteworthy:
#
# 1. multi line strings
# 2. escape sequences (raw)
# 3. comparison
# 4. subscripting
# 5. formatting strings to print
# 6. formatting numbers to print
#***********************************************

#************************************
#Multiline strings
#End of lines are preserved unless removed with an escape \ 
#************************************
multilineString = """First line
Second line
third line
"""
print (multilineString)

#************************************
#Glued strings
#No need for + if next to each other
#************************************
msg2 = "test" + "another test"
msg3 = "test" "another test"
print (msg2)
print (msg3)

#You have to put them in brackets to make the following work
msg4 = ("test"
    "another test string"
    "and one more string")
#All these strings will be concatenated
#Note: there will be no line separators

print (msg4)

#************************************
#Agreeing with escapes
#************************************
msg5 = r"c:\rootdir\otherdir"
msg6 = "c:\\rootdir\\otherdir"

#************************************
#Comparing strings
#************************************

if msg5 == msg6:
    print ("yes they are same")
else:
        print("No, they are not the same")

print (msg5)
print (msg6)

#************************************
#Finding strings using "in" key word
#************************************
available1 = r"c:\root" in msg5
available2 = "c:\root" in msg5
print (available1)
print (available2)

#************************************
#Subscripting
#************************************ 
msg5 = "0123456789"
msg7 = msg5[:4] #Get 0 to 3
print (msg7)

#Notice how it gets the 5th character
#as the array is 0 based
msg8 = msg5[4:8] #4,5,6,7
print (msg8)    
c7th = msg5[6]
print (c7th) #You will get 6

#************************************
#Length
# len() is what is called a Built in function
#************************************ 
print (len(msg5)) #should be 10

#************************************
#Cases: Title, Upper, Lower
#************************************ 
msg9 = "how ABOUT This sEntence"
print (msg9.title()) #How About This Sentence
#Each word starts with an upper case

print (msg9.upper()) 
print (msg9.lower()) 

#************************************
#Formatting
#************************************ 
x = 10
y = "hello there"

fs = str.format("begin {0} and end with {1}",y.upper(),x)
print(fs)

fsTemplate = "begin {0} and end with {1}"
print(fsTemplate.format(y.upper(),x))

complexNum = 10 + 2j
print(complexNum)

fs = "real {0.real}, and imaginary {0.imag}".format(complexNum)
print(fs)

#************************************
# Additional formatting options
# {!r,s,a} conversions
# {:} format specs
#
# The {!r,s,a} conversions first.
#************************************ 
s = "test string"
fs = "The r: {0!r}, the s: {0!s}, the a: {0!a}".format(s)
print(fs)

# will print the below line
#
# The r: 'test string', the s: test string, the a: 'test string'
#
# notice the quotes for "r" part and "a" part
#
# !r calls the repr() function on the object
# !s calls the str() function
# !a calls the ascii() function

#lets try this on a type object
t = type(s)
fs = "The r: {0!r}, the s: {0!s}, the a: {0!a}".format(t)
print(fs)

# will print the below line
#
# The r: <class 'str'>, the s: <class 'str'>, the a: <class 'str'>
#
# it is the string representation of the object
#

#let me do this on a list
l = (1,2,3)
fs = "The r: {0!r}, the s: {0!s}, the a: {0!a}".format(l)
print(fs)

# will print the below line
#
# The r: (1, 2, 3), the s: (1, 2, 3), the a: (1, 2, 3)
#

#let me do this on a number
f = 0.24
fs = "The r: {0!r}, the s: {0!s}, the a: {0!a}".format(f)
print(fs)

# will print the below line
#
# The r: 0.24, the s: 0.24, the a: 0.24
#

#************************************
# {:} format specs: next
#
# With this you can control
# 1. alignment 
# 2. sign
# 3. fill character
# 4. width
# 5. precision of after decimals
# 6. number format (binary, decimal etc.)
# 7. exponent, fixed point, percentages
#************************************ 

#***********************
# Right aligned text
#***********************
s = "right aligned"
n = 100
#allocate a width of 30 characters and right align text
fs = ("Right aligned {:>30}").format(s)
print (fs)

# prints the following
# Right aligned                  right aligned

#***********************
# Right aligned number
#***********************
fs = ("Right aligned {:>30}").format(n)
print (fs)

# prints the following
# Right aligned                            100

#***********************
# Right aligned number with a different fill than a space
#***********************
fs = ("Right aligned {:*>30}").format(n)
print (fs)

# prints the following, where the filler is "*"
#Right aligned ***************************100

#***********************
# For numbers: Lead with #
# number
# width
# Comma separator
# filler "0"
#***********************
int_n = 10000
float_n = 23.45678

# an integer with a width of 30
fs = ("integer 10,000 with width of 30 {:#30}").format(int_n)
print (fs)
#integer 10,000 with width of 30                          10000

#float with a width of 30
fs = ("Decimal 23.456 width of 30 {:#30}").format(float_n)
print (fs)
#Decimal 23.456 width of 30                       23.45678

#float with width and filler of 0
fs = ("Decimal 23.456 width of 30 with fillers of 0: {:#030}").format(float_n)
print (fs)
#Decimal 23.456 width of 30 with fillers of 0: 000000000000000000000023.45678

#float with width and filler of 0 and thousands separator of ","
fs = ("Decimal 23.456 width of 30 with fillers of 0: {:#030,}").format(float_n)
print (fs)
#Decimal 23.456 width of 30 with fillers of 0: 0,000,000,000,000,000,023.45678

#float with width and filler of 0 and thousands separator of "_"
fs = ("Decimal 23.456 width of 30 with fillers of 0: {:#030_}").format(int_n)
print (fs)
#Decimal 23.456 width of 30 with fillers of 0: 00_000_000_000_000_000_010_000

#Only , and _ and "n" are allowed as separators
#it is not clear wht "n" does as it seem to behave as if nothing is specified


