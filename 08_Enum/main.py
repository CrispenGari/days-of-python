
from enum import Enum

class Colors(Enum):
    red = 1
    blue = 2
    green = 3
print([c.name for c in Colors]) ## ['red', 'blue', 'green']