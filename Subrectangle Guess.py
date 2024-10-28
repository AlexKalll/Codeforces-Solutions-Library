def main():
    num_tests = int(input())

    for _ in range(num_tests):
        n, m = map(int, input().split())
        grid = []

        max_i, max_j = 0, 0

        for i in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
            for j in range(m):
                if row[j] > grid[max_i][max_j]:
                    max_i, max_j = i, j

        h = max(max_i + 1, n - max_i)
        w = max(max_j + 1, m - max_j)
        print(h * w)

if __name__ == "__main__":
    main()
