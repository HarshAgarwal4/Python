# f=open("this.txt")
# data=f.read()
# print(data)
# f.close()

# st='hello heqwj'
# f=open('this.txt' , 'w')
# f.write(st)
# f.close()

with open("this.txt" , 'r+') as f:
    text = f.read()
    f.write("Hello")
    print(text)
