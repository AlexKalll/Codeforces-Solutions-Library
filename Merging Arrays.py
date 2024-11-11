n, m = map(int, input().split())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

merged_array = []
i, j = 0, 0

# Merge the two arrays using two pointers
while i < n and j < m:
    if array_a[i] <= array_b[j]:
        merged_array.append(array_a[i])
        i += 1
    else:
        merged_array.append(array_b[j])
        j += 1

# If there are remaining elements in array_a
while i < n:
    merged_array.append(array_a[i])
    i += 1

# If there are remaining elements in array_b
while j < m:
    merged_array.append(array_b[j])
    j += 1

# Output the merged array
print(*merged_array)
