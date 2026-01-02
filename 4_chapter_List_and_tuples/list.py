friend = ['apple' ,"orange" , 5 , 38.40 , False , [1,2]]
print(type(friend[5]))

print(friend[0])
friend[0] = "Grapes"
print(friend[0])        # muttable
print(friend[1:4])
friend.pop(3)
print(friend)