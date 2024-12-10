t = int(input())

for _ in range(t):
      x, y, n = map(int, input().split())
      q = n // x
      mode = n % x
      ans = x * q + y 
      if ans <= n:
            print(ans)
      else:
            print(x * (q - 1) + y)
