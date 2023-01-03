import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
lst = []
visited=[False]*n

def dfs(start):
    if start == m:
        print(' '.join(map(str, lst)))
        return
    remember = 0
    for i in range(len(nums)):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            lst.append(nums[i])
            remember = nums[i]
            dfs(start + 1)
            visited[i] = False
            lst.pop()

dfs(0)