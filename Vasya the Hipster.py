red, blue = map(int, input().split())
total = red + blue
a = min(red, blue)
total -= 2 * a
b = total // 2

print(a, b)
