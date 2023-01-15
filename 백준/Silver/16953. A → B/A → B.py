import sys
from collections import deque


def bfs(root):
    queue = deque([[root, 1]])

    while queue:
        n, l = queue.popleft()
        if n > target:
            continue

        if n == target:
            return l

        queue.append([n * 2, l+1])
        queue.append([int(str(n)+str(1)), l+1])
    else:
        return -1


s, target = map(int, sys.stdin.readline().split())
print(bfs(s))