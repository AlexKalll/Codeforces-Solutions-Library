n, m = map(int, input().split())
colored = False

for _ in range(n):
      colors = set(input().split())
      for color in colors:
            if 'W' != color and 'B' != color and  'G' != color:
                  colored = True
                  break
            if colored:
                  break            
if colored:
      print('#Color')
else:
      print('#Black&White')
