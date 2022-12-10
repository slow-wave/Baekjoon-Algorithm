import sys

def memo(n):
    dp = [0 for i in range(12)]

    dp[0], dp[1], dp[2] = 1, 2, 4

    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    return dp[n-1]

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        print(memo(int(sys.stdin.readline())))