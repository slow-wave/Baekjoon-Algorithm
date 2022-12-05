import sys
from collections import deque

def bfs(root, start):
    num = [0] * (N + 1)
    visited = [start]

    queue = deque([start])

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if i not in visited:
                num[i] = num[n] + 1
                visited.append(i)
                queue.append(i)

    return sum(num)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N+1)]
    result = []

    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        result.append(bfs(graph, i))

    print(result.index(min(result))+1)