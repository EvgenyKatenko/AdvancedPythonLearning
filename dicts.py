#Dictionary: key-value pairs, unordered, mutable

mydict = {"name" : "Evgeny", "age" : 35, "hometown" : "Khabarovsk"} 

mydict2 = dict(name = "Max", age = 34, hometown = "Komsa")

print(mydict)
print(mydict2["name"])

del mydict["name"]
print(mydict)

'''
.pop
.popitem
'''

if "name" in mydict2:
    print(mydict2["name"])

for k,v in mydict.items():
    print(f'{k} : {v}')

# copying: deep vs shallow
# .copy() for deep or dict(...)

# .update() for overwriting with another dict