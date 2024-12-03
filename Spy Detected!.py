t = int(input())

for i in range(t):
      arrLen =  int(input())
      arr = list(map(int,input().split()))
      spy = {}
      for item in arr:
            if item in spy:
                  spy[item] += 1
            else:
                  spy[item] = 1
      for k, v in spy.items():
            if v == 1:
                  for idx, m in enumerate(arr, start=1):
                        if m == k:
                              print(idx)
