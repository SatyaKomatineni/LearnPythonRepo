
from baselib import baselog as log

"""
*************************************************
* To implement generics, import the following
*************************************************
"""
from typing import Generic, TypeVar

"""
*************************************************
* Define tyype variables
*************************************************
"""
# Define two type variables, T and U, which can be any types
T = TypeVar('T')
U = TypeVar('U')

"""
*************************************************
* Use type variable to parameterize classes
*************************************************
"""
# Define a generic class Pair, which can hold two items of types T and U
class Pair(Generic[T, U]):
    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second

    def get_first(self) -> T:
        return self.first

    def get_second(self) -> U:
        return self.second

    def __repr__(self) -> str:
        return f'Pair({self.first!r}, {self.second!r})'

"""
*************************************************
* Use the new type
*************************************************
"""
def _test1():
    pair1: Pair[int,int] = Pair(5,6)
    log.ph("Testing int, int pair", pair1)

def _test2() -> Pair[str,str] :
    return Pair("first", "second")

def _test3():
    pair: Pair[str,str] = _test2()
    log.ph("Testing string, string pair", pair)

def _test4():
    log.ph1("Broader test")
    # Pair of an integer and a string
    pair_int_str = Pair(1, "Apple")
    print(pair_int_str)

    # Pair of a string and a list of floats
    pair_str_list = Pair("Temperatures", [32.5, 31.8, 30.2])
    print(pair_str_list)

    # Accessing elements
    print(pair_int_str.get_first())  # Output: 1
    print(pair_int_str.get_second())  # Output: Apple
    print(pair_str_list.get_second())  # Output: [32.5, 31.8, 30.2]

def _test():
    _test1()
    _test3()
    _test4()

def localTest():
    log.ph1("Starting local test")
    _test()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()