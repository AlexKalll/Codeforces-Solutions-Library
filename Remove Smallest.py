t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    if n == 0:
        print("NO")
    for i in range(n-1):
        if arr[i+1] - arr[i] > 1:
            print("NO")
            break
    else:
        print("YES")
    
