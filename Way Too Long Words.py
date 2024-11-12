t = int(input())

for _ in range(t):
    word = input()
    if len(word) > 10:
        short = word[0] + str(len(word[1:-1])) + word[-1]
        print(short)
    else:
        print(word)
