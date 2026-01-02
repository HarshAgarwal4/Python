a=set()  #empty set
a = {}   #empty dictionary
a = {1,2,3,4,4,4}
print(a)

a.add(5)
print(a)
print(len(a))

a.remove(5)
print(a)

print(a.pop() , a)
a.clear()
print(a)

a= {1,2,3,4}
a= a.union({5,6})
print(a.union({5,6}))

b={2,3,10,12}
print(a.intersection(b))