n = int(input())
base = 1
c = 2
t = 0

while n - base >= 0:
      n -= base
      base += c
      c += 1
      t +=1

print(t)
