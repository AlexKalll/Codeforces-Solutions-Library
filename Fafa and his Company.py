# https://codeforces.com/problemset/problem/935/A

n = int(input())
ways = 0

for i in range(1, n):
      if  (n - i) % i == 0:
            ways += 1
print(ways)
