
from baselib import baselog as log

"""
*************************************************
* string concat test
*************************************************
"""
def testStringConcat():
    x = "hello"; y = 10
    y = x
    z = x + y
    print (z);

def opArgFunction(arg1: str, arg2: str | None = None):
    log.ph1("Op args")
    log.info(arg1)
    if not arg2 is None:
        log.info(arg2)

from typing import Optional
def opArgFunction2(arg1: str, arg2: Optional[str] = None):
    log.ph1("Op args")
    log.info(arg1)
    if not arg2 is None:
        log.info(arg2)

def test():
    testStringConcat()
    opArgFunction("Hello")
    opArgFunction2("Hello")

def localTest():
    log.ph1("Starting local test")
    test()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()