"""
*************************************************
* Explain generics
*************************************************
"""
from baselib import baselog as log


#need for old generics < 3.5
from typing import List
def testOldGenericLists():
    oldlist: List[int] = [1,2,3] # This is an old generics
    #oldlist.append("hello") #fails type check, runs ok
    oldlist.append(5) # good
    print(oldlist)

def testNewGenericLists():
    newlist: list[int] = [4,5,6] # new one is native
    #newlist.append("hello") #fails type check, runs ok
    newlist.append(5) # good
    print(newlist)

"""
*************************************************
* Key points

1. list[int] is the basic generics syntax
2. The class "list" is already a genericized class
3. Classes you genericize will also be used this way

*
*************************************************
"""
def test():
    testOldGenericLists()

def localTest():
    log.ph1("Starting local test")
    test()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()