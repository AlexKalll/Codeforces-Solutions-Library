# https://codeforces.com/problemset/problem/155/A

n = int(input())
contests = list(map(int, input().split()))
best = contests[0]
worst = contests[0]
count = 0

for idx, score in enumerate(contests, start=1):
      if score > best:
            best = score
            count += 1
      elif score < worst:
            worst = score
            count += 1

print(count)
