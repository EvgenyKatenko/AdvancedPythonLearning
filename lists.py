mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "Apple", "Apple"]
print(mylist2)

mylist3 = [1,2,3,4,5,6,7,8,9]
def power2(x):
    return x**2
print(list(filter(lambda x: x >= 5, map(power2,mylist3))))
print([x for x in mylist3 if x >=5])

if 5 in mylist2:
    print("YES")
else:
    print("NO")

print(len(mylist3))

mylist3.append("Spartak")
mylist3.insert(1,111)
print(mylist3)

mylist4 = mylist3.pop()
print(mylist3)

'''
.remove()
.clear()
.sort()
sorted(list)
'''

mylist5 = [0] * 5
print(mylist5)

'''
lists concatination / union via "+"
'''

mylist6 = mylist3[1:6:-1]
print(mylist6)