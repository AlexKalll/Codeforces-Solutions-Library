n, k = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for num in query:
    l, r = 0, len(arr) - 1
    while l <= r: 
        mid = (l+r) // 2  
        if arr[mid] == num:
            print('YES')
            break
        elif arr[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    else:
        print('NO')
   #Time complexity: O( k * log(n))    
  """
# just by using the built in method bisect which is more efficient one
from bisect import bisect_left
n, k = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

for num in query:
    idx = bisect_left(arr, num)
    if 0 <= idx < n:
        if arr[idx] == num:
            print('YES')
        else:
            print('NO')
            
            """
