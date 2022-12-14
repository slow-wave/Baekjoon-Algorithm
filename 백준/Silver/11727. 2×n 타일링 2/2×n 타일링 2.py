import sys

def memo(n):
    dp = [0] * 1001
    dp[1], dp[2], dp[3], dp[4] = 1,3,5,11

    if n <= 4:
        return dp[n]

    for i in range(5, n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2

    return dp[n]


n = int(sys.stdin.readline())
print(memo(n) % 10007)