import sys

def memo(arr, k, n):
    for i in range(n):
        arr[0][i] = i + 1

    for a in range(1, k+1):
        for b in range(n):
            arr[a][b] = arr[a-1][b] + arr[a][b-1]

    return arr[k][n-1]


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    for _ in range(n):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())

        arr = [[0 for _ in range(n)] for _ in range(k+1)]
        print(memo(arr, k, n))