"""
*************************************************
* Explain generics: lesson 2
* 
* 1. You have to enable strick typing
* 2. MyList2(list[Person]): means I am extending person list
* 3. MyList(Generic[Person]): will not work
* 4. MyList(Generic[TypeVar("T", bound=Person)]) will work
* 5. See code below
*
* Note: Doesn't seem like a good example
*
*************************************************
"""
from baselib import baselog as log

from typing import TypeVar, Generic
class Person():
    def __init__(self, name: str):
        self.name = name
    def __repr__(self) -> str:
        return self.name


#
# You are saying my class works with "person" objects
# It is NOT saying I am a list of Persons
# Note: you have to enable strict typing to see the implications
#

T = TypeVar ("T", bound=Person)
class MyList(Generic[T]):
    persons: list[T] = []
    def addPerson(self, obj: T):
        self.persons.append(obj)

# Extending a list of persons
class MyList2(list[Person]):
    pass

class Organization(list[Person]):
    def __init__(self, name:str, address:str):
        self.name = name
        self.address=address

    # The __dict__ holds the key value pairs of self
    # such as name, address etc.
    def __repr__(self) -> str:
        t = (self.__dict__, super().__repr__())
        return f"{t}"

def testOrgainzation():
    org = Organization("MyOrg","111, 1st Street, Great City")
    org.append(Person("name1"))
    org.append(Person("name2"))
    org.append(Person("name3"))
    print(org)

class Organization2(Generic[T]):
    def __init__(self, name:str, address:str):
        self.name = name
        self.address=address
        self.list: list[T] = []

    def add(self, p: T):
        self.list.append(p)

    # The __dict__ holds the key value pairs of self
    # such as name, address etc.
    def __repr__(self) -> str:
        t = (self.__dict__, super().__repr__())
        return f"{t}"


def testOrgainzation2():
    org = Organization2[Person]("AnOrg","111, 1st Street, Great City")
    org.add(Person("name1"))
    # org.add("hello") will fail
    print(org)

"""
# won't work
class MyList3(Generic[Person]):
    pass
    
"""

def testPList():
    personList = MyList[Person]()
    #This will not work below if strict typing is enabled
    #personList.addPerson(1)
    personList.addPerson(Person(name="satya"))
    print(personList.persons)

def testPList2():
    personList = MyList2()

    #fails
    #personList.append(1234)

    #succeeds
    personList.append(Person(name="satya"))
    print(personList)

def localTest():
    log.ph1("Starting local test")
    testPList()
    testPList2()
    testOrgainzation()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()