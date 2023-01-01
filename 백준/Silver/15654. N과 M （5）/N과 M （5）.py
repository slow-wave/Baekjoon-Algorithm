import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
lst = []

def dfs(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    # for i in range(start, n+1):
    for i in range(len(nums)):
        if nums[i] not in lst:
            lst.append(nums[i])
            dfs(nums[i])
            lst.pop()
dfs(nums[0])