given=input()
small_letters=set()
for i in given:
    if 97<=ord(i)<=122:
        small_letters.add(i)
print(len(small_letters))

#another way of implimentation
'''
given = input()
small_letters = {char for char in given if char.islower()}
print(len(small_letters))
'''