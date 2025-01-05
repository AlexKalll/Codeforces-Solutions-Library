# https://codeforces.com/problemset/problem/1369/A

t = int(input())
yes = 'YES'
no = 'NO'

for _ in range(t):
      n = int(input())
      if n % 4 == 0:
            print(yes)
      else:
            print(no)
