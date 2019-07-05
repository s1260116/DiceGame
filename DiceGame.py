import random
from functools import reduce

name = input('What is your name?\n')

print(f'Hello, {name}!')

print('Rolling the dice...')

dice = [(1,random.randint(1,6)), (2,random.randint(1,6))]

for x in dice: print('Die %d: %d' % x)

print('Total value:', reduce(lambda x, y: x[1]+y[1], dice))
