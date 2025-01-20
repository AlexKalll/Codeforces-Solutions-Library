# https://codeforces.com/problemset/problem/705/A

n = int(input())

# Define the phrases to be used based on the index
edgeOdd = 'I hate it'
edgeEven = 'I love it'
middleOdd = 'I hate that'
middleEven = 'I love that'

# Loop through each index from 1 to n
for i in range(1, n + 1):
    # If n is 1, print the edgeOdd phrase
    if n == 1:
        print(edgeOdd, end=' ')
    # Check if we are at the last index
    elif i == n:
        # Print edgeEven if n is even, else print edgeOdd
        print(edgeEven, end=' ') if n % 2 == 0 else print(edgeOdd, end=' ')
    else:
        # Print middleEven for even indices, middleOdd for odd indices
        print(middleEven, end=' ') if i % 2 == 0 else print(middleOdd, end=' ')
