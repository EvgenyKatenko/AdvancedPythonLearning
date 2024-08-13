# Lambda arguments: expression 

from functools import reduce

def add10Func(x):
  return x+10

def distFunc(p):
  #map
  res = map(lambda x : x**2, p)
  #reduce
  sumElems = reduce(lambda x,y: x+y,res)
  return sumElems


add10 = lambda x : x + 10
mult = lambda x,y : x*y

print(add10Func(5))
print(mult(12,11))

#sorterd, map, filter, reduce

#sorting
points2D = [(1,2),(15,1),(5,-1),(10,4)]
points2D_sorted = sorted(points2D, key = lambda p: p[0]**2 + p[1]**2)
points2D_sorted = sorted(points2D, key = distFunc)
print(points2D)
print([points2D_sorted])

#filter
a = [1,2,3,4,5,6,7]
b = filter(lambda x : x % 2 == 0, a)
b1 = [x for x in a if x % 2 == 0]
print(list(b1))

#reduce
c = reduce(lambda x,y : x * y, a)
print(c)