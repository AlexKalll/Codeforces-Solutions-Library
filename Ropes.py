n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

def checker(t):
    count = 0
    for rope in a:
        cur = rope / t
        count += int(cur)
    return count >= k

l, r = 0, max(a)

while r - l > 0.000001:
    mid = (l + r) / 2
    if checker(mid):
        l = mid
    else:
        r = mid

print(l)

# Time Complexity: O(n * log(max(a))) 
# Space Complexity: O(1)
