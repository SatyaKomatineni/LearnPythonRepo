#*********************************************
# Lesson 3: 
# Functions
#
# full list at: https://docs.python.org/3.7/library/functions.html
#
# Noteworthy:
#
# 1. Create a function
# 2. ":" and tabs
# 3. Arguments
#
#***********************************************

#******************************
# Few simple functions
#******************************

def printBeginMsg(msg):
    print ("*****************************")
    print ("* " + msg)
    print ("*****************************")

def printEndMsg(msg):
    print ("*****************************")
    print ("* " + msg)
    print ("*****************************")

def printCollected(msg, aSequenceOrAList):
    printBeginMsg(msg)
    for item in aSequenceOrAList:
        print (item)
    printEndMsg(msg)

#fun with renaming functions
def ph(msg):
    printBeginMsg(msg)

def pf(msg):
    printEndMsg(msg)

def p(msg):
    print(msg)

def pc(msg, sequence):
    printCollected(msg,sequence)

#***********************************
# Function notes: 
#
# The : and tabs
#   1. A ":" at the end of a line starts a scope
#   2. All subsequent lines that are indented at the same level is part of that scope
#   3. A new line that goes back to the parent indent level ends that scope
#***********************************

ph("This is a header")
p("line1");p("line2");p("line3")
pf("End of message")

x = 10,12,14

pc("This is a sample collection", x)