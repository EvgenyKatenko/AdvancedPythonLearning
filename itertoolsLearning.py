# itertools: product, permutations, accumulate, groupby, infinite iterators

from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=1)
print(list(prod))

from itertools import permutations
c = [1,2,3]
perm = permutations(c, 3)
print(list(perm))

from itertools import combinations #can also do with replacement
d = [1,2,3,4]
comb = combinations(d, 2)
print(list(comb))

from itertools import accumulate
import operator
n = [1,2,3,4,5,6]
#acc = accumulate(n)
acc = [x for x in accumulate(n, func = operator.mul)]
print(acc)

from itertools import groupby
a = [1,2,3,4]
gr = groupby(a, key = lambda x : x < 3)
for k,v, in gr:
    print(f'{k} : {list(v)}')

people = [
    {'name' : 'Ivan', 'age' : 25},
    {'name' : 'Evgeny', 'age' : 25},
    {'name' : 'Max', 'age' : 30},
    {'name' : 'John', 'age' : 50}
]

people_gr = groupby(people, key = lambda x : x['age'])
for k,v, in people_gr:
    print(f'{k} : {list(v)}')


from itertools import count, cycle, repeat
for idx in count(10):
    print(idx)
    if (idx > 15):
        break

a = [1,2,3]
cycleNum : int = 0
for idx in cycle(a):
    print(idx)
    cycleNum += 1
    if (cycleNum > 10):
        break