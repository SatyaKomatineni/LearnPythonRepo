
from baselib import baselog as log

from pydantic import BaseModel, Field
#from pydantic import EmailStr
from pydantic.functional_validators import AfterValidator

from typing import Any
from typing_extensions import Annotated
import re

"""
*************************************************
* Test phone number
*************************************************
"""


def _validatePhoneNumber(phone_number: str) -> str:
    pattern = r'^(?:\+?1)?[ -.]?\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{4}$'
    if re.match(pattern, phone_number) is not None:
        return phone_number + ", A US Phone number"
    msg = f"{phone_number} is invalid"
    raise ValueError(msg)

# "+1 (123) 456-7890"

def _testPhone(phone: str):
    try:
        _validatePhoneNumber(phone)
    except ValueError as e:
        print(e)

def _testPhones():
    _testPhone("+1 (123) 456-7890")
    _testPhone("123-456-9000")
    _testPhone("1234569000")

USPhone = Annotated[str, AfterValidator(_validatePhoneNumber)]
#USPhone = Annotated[str, Field(pattern=r'^(?:\+?1)?[ -.]?\(?\d{3}\)?[ -.]?\d{3}[ -.]?\d{4}$')]

class User1(BaseModel):
    id: int
    name: str = 'Jane Doe'
    phone: USPhone

def _testUser1():
    u1 = User1(id=1,phone="+1 (123) 456-7890")
    u2 = User1(id=1,phone="+1 (123) 456-7890")

    log.ph("u1",u1)
    log.ph("u2",u2)

    #The following will throw an error
    #u3 = User1(id=1,phone="+1 (123) 456-78")
    #log.ph("u3",u3)
"""
*************************************************
* Simple Validators
*************************************************
"""
def _double(n: int):
    return 2 *n

DoubledNumber = Annotated [int, AfterValidator(_double)]

class DoubledNumbers(BaseModel):
    number1: DoubledNumber

def testDoubledNumber():
    n = DoubledNumbers(number1=5)
    print(n)



"""
*************************************************
* Simple class with initializations
*************************************************
"""
# Define the class
class User(BaseModel):
    id: int
    name: str = 'Jane Doe'



def testBasics():
    #instantiate the class
    # u = User() # gives an error
    # u = User(1) # Doent' honor positional args
    u = User(id=1)

    modelDumpDict: dict[str, Any] = u.model_dump()
    modelDumpJson: str = u.model_dump_json()
    jsonSchema: dict[str, Any] = u.model_json_schema()

    log.ph("Plain string", modelDumpDict)
    log.ph("json", modelDumpJson)
    log.ph("json schema", jsonSchema)
    log.ph("Class as is",u)
    

def test():
    #testBasics()
    #testDoubledNumber()
    #_testPhones()
    _testUser1()

def localTest():
    log.ph1("Starting local test")
    test()
    log.ph1("End local test")

if __name__ == '__main__':
    localTest()