#sets : unorders, mutable, unique elements

myset = {1,2,3,4,"HI"}
print(myset)

myset1 = set(["Hello"])
print(myset1)

myset.discard(2)
print(myset)

myset.pop()
print(myset)

myset.clear()
print(myset)

evens = {2,4,6,8}
odds = {1,3,5,7,9}
naturs = set(x for x in range(1,10))
print(naturs.intersection(odds))

print(naturs.difference(evens).difference(odds))

print(naturs.symmetric_difference(odds.union(evens)))

setA = {1,2,3,4,5,6,7,9}
setB = {1,2,3,10,11,12,13}
#setA.update(setB)
setA.intersection_update(setB)
#difference_update
print(setA)

setA = {1,2,3,4,5,6,7,9}
setB = {1,2,3}
print(setB.issubset(setA))
print(setA.issuperset(setB))

#frozen set = immatable
setC = frozenset([1,2,3,4,5])
print(setC)
