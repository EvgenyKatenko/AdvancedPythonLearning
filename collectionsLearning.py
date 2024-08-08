# collections: counter, namedtuple, OrderedDict, defaultdict, deque

# COUNTER
from collections import Counter
someString : str = 'aaaabbbccc'
myCounter : Counter = Counter(someString)

print(myCounter)
print(myCounter.most_common(1))
print(list(myCounter.elements()))
print(myCounter.total())

print('-------------------------------------------------')
######################## 

# Name tuple
from collections import namedtuple
Point2D = namedtuple('Point2D', ['x','y'])
pt : Point2D = Point2D(1,-3)
print(pt)
print(f'x = {pt.x}, y = {pt.y}')

print('-------------------------------------------------')
######################## 

#Ordered dict 
from collections import OrderedDict
ordDict : OrderedDict = OrderedDict()
ordDict['a'] = 1 
ordDict['b'] = 111 
ordDict['c'] = 16 
ordDict['d'] = 12 
ordDict['e'] = 11 
print(ordDict)

print('-------------------------------------------------')
######################## 

#Default dict 
from collections import defaultdict
d : defaultdict = defaultdict(int) #sets int for default key -> value
d['a'] = 1
d['b'] = 2
for v in d:
    print(f'{v} : {d[v]}')
print(f'xxx : {d["xxx"]}')

print('-------------------------------------------------')
######################## 

#Deque
from collections import deque

d : deque = deque()
d.append(1)
d.append(2)

print(d)

d.appendleft(0)
print(d)

d.popleft()
print(d)

d.pop()
print(d)

d.extendleft([11,22,33])
print(d)

d.rotate(1)
print(d)