import math

n = int(input())
for _ in range(n):
    l, r = map(int, input().split())

    exp = math.floor(math.log2(r))
    if 2**(exp+1) - 1 == r:
        print(r)
        continue

    print(2**(exp) - 1)
