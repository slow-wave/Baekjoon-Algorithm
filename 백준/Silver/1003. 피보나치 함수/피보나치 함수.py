import sys


def memo_fibo(n):
    memo[0] = [1, 0]
    memo[1] = [0, 1]

    if n < 2:
        return memo[n]

    for i in range(2, n + 1):
        memo[i][0] = memo[i - 2][0] + memo[i - 1][0]
        memo[i][1] = memo[i - 2][1] + memo[i - 1][1]
    return memo[n]


i = int(sys.stdin.readline())
for _ in range(i):
    n = int(sys.stdin.readline())
    memo = [[0, 0] for i in range(n + 2)]
    print(memo_fibo(n)[0], memo_fibo(n)[1])