from logging import lastResort
from os import remove

numbers = [12, 45, 7, 45, 32, 18, 9]
value=45

if value in numbers:
    print(numbers.index(value))
