import sys

def memo(n):
    dp = [0] * 1001
    dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 5

    if n <= 3:
        return dp[n]

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


n = int(sys.stdin.readline())
print(memo(n) % 10007)