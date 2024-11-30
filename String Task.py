word = input()
output = []
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

for letter in word.lower():  # codeforces / tour
    if letter in vowels:
        pass
    else:
        output.append(letter)  # Append the letter to the output list

output = '.' + '.'.join(output)

print(output)
