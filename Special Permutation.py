t = int(input())

for _ in range(t):
    n = int(input())
    if n < 4:
        print(-1)
        continue
    
    # Print odd numbers in descending order
    for i in range(n, 0, -1):
        if i % 2 == 1:
            print(i, end=" ")
    
    # Print 4 and 2
    print(4, 2, end=" ")
    
    # Print even numbers starting from 6
    for i in range(6, n + 1, 2):
        print(i, end=" ")
    
    print()  # New line at the end of each test case
