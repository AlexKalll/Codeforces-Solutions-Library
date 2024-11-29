from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
ans = 0
count = defaultdict(int)

for r in range(n):
    count[a[r]] += 1
    while len(count) > k:
        count[a[l]] -= 1

        if count[a[l]] == 0:
            del count[a[l]]
        l += 1
    ans += r - l + 1

print(ans)
