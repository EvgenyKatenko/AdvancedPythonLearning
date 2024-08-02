# TUPLE: ordered, immutable, allows duplicate elements


#Creation
mytup1 = ("Max",77,"Russia")
print(mytup1)

mytup2 = tuple([1,2,3,4])
print(mytup2)

print(mytup2[1])

#Elements

for x in mytup1:
    print(x)

print(len(mytup2))
print(mytup2.count(1))
'''
.index(elem)
'''

#tuple -> list
mylist = list(mytup2)
print(mylist)

#slicing is the same as in lists

#unpacking
a,b,c = mytup1 
print(b)

d1, *d2 = mytup1
print(d2)