# with open("poems.txt") as f:
#     text = f.read()
#     if('twinkle' in text): print("twinkle word present in file")
#     print(text)


# import random
# def game():
#     print("You are playing game ...")
#     h_score = random.randint(1,100)
#     print("Your current score = ",h_score)
#     with open("h-score.txt") as f:
#         text = f.read()
#         if(text != ""):
#             print("Previous high score = ", text)
#             if(h_score > int(text)):
#                 print("Congrats! You acheived new high score")
#                 with open("h-score.txt" , 'w') as h:
#                     h.write(str(h_score))
#             else:
#                 print("better luck next time")
#         else:
#             print("No previous high score")
#             with open("h-score.txt" , 'w') as h:
#                 h.write(str(h_score))
#     return h_score
# print("current high score =" , game())

# def tableInFile(n):
#     name = str(n) + '_ki_Table.txt'
#     with open("Tables/" + name , "a") as f:
#         with open("Tables/" + name , 'r') as g:
#             text = g.read()
#             if(text == ""):
#                 line = "Table of "+str(n)+" :-\n\n"
#                 f.write(line)
#         for i in range (1,11):
#             line = str(n)+" x "+str(i)+" = "+str(n*i)+"\n"
#             f.write(line)

# for i in range(2,21):
#     tableInFile(i)

# word="Donkey"
# def check(word):
#     with open("check.txt") as f:
#         text=f.read()
#         print("original text is :-\n",text)
#         if(word in text):
#             text = text.replace(word , "#"*len(word))
#             print(text)
#             with open("check.txt" , "w") as g:
#                 g.write(text)
#         else: print("Word not found in text")

# check(word)

# words = ['sex' , 'sux' , 'naked' , 'fuck' , 'cum']
# def check(word):
#     with open("check.txt") as f:
#         text=f.read()
#         # print("original text is :-\n",text)
#         if(word in text):
#             text = text.replace(word , "#"*len(word))
#             # print(text)
#             with open("check.txt" , "w") as g:
#                 g.write(text)
#         else: print("Word not found in text")

# for item in words:
#     check(item)