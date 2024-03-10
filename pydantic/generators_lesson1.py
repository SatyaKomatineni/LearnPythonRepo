from typing import (
    Any,
    Generator
)

def count_up_to(max: int):
    count = 1
    while count <= max:
        yield count
        count += 1
    print("End of iteration")

def testGen():
    gen: Generator[int, Any, None] = count_up_to(2)
    x = next(gen)
    y = next(gen)
    print(x,y)
    
    #This will thorw StopIteration
    #z = next(gen)
