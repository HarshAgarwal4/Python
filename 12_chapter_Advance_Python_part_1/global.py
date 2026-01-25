a=100

def fun():
    global a
    a=4
    return a

print(fun())
print(a)

#enumerate

list = [1,2,3,4]
for i,item in enumerate(list):
    print(i,item)



