import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
lst = []


def dfs(start):
    if start == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(n):
        if start == 0 or lst[start - 1] <= nums[i]:
            lst.append(nums[i])
            dfs(start + 1)
            lst.pop()


dfs(0)