from typing import Generic, TypeVar

# Define base classes
class BaseT:
    pass

class BaseU:
    pass

# Define type variables with bounds
T = TypeVar('T', bound=BaseT)
U = TypeVar('U', bound=BaseU)

# Define a generic class Pair with type variables T and U
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

# Example subclasses of BaseT and BaseU
class DerivedT(BaseT):
    def __repr__(self):
        return "DeriverT instance"

class DerivedU(BaseU):
    def __repr__(self):
        return "DeriverU instance"

# Usage with derived types
pair = Pair(DerivedT(), DerivedU())
print(pair)