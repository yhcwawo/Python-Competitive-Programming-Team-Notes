## pratice.py == replit main.py for Algorithm test

from itertools import permutations
from itertools import combinations
import math

array = [i for i in range(10)]

print(array)
sets = {1, 2 }

result = [i for i in array if i not in sets]
print(result)



def add(a,b):
    return a+b


print( add(3,5))

print(min(array))
print(max(array))

arrayi = [('홍길동', 35),('윤홍찬', 30), ('문태민', 32)]

print(sorted(arrayi,key=lambda x: x[1], reverse=False))


data = ['a','b','c']

results = list(permutations(data, 3))
results = list(combinations(data, 3))
print(results)


def lcm(a,b):
  return a * b // math.gcd(a,b)