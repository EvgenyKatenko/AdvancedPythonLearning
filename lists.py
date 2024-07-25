mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "Apple", "Apple"]
print(mylist2)

mylist3 = [1,2,3,4,5,6,7,8,9]
def power2(x):
    return x**2
print(list(filter(lambda x: x >= 5, map(power2,mylist3))))
print([x for x in mylist3 if x >=5])