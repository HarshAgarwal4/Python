import pyjokes as jokes
import os

joke = jokes.get_jokes()
path = r'C:\Users\Dell\Desktop'
a = os.listdir(path)

#single line comment

"""
multi line comment
"""
for item in joke:
    print(item)

for item in a:
    print(a)