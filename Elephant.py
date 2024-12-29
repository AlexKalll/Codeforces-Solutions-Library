# https://codeforces.com/problemset/problem/617/A

x = int(input())
print(x//5 if x%5 == 0 else x//5 + 1)
