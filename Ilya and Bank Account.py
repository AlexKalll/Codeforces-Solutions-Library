# https://codeforces.com/problemset/problem/313/A

n = input()
original = list(n)
case1 = int(''.join(original[:-1]))
case2 =  int(''.join(original[:-2] + [original[-1]]))

print(max(int(n), case1, case2)) 
