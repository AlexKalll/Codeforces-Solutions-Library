def largest_frame_side_length(w, b):
    k = 0
    while (k * (k + 1)) // 2 <= w + b:
        k += 1
    k -= 1
    return k

t = int(input())
for _ in range(t):
    w, b = map(int, input().split())
    print(largest_frame_side_length(w, b))
