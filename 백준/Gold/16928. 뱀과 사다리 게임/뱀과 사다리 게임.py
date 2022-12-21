import sys
from collections import deque

def bfs(g):
    visited = [0 for _ in range(100)]

    queue = deque([[0, 0]])

    while queue:
        x, v = queue.popleft()

        for d in range(1, 7):
            dx = x + d

            if g[dx]:
                dx = g[dx]

            v = dx

            if dx >= 100:
                continue

            if not visited[dx]:
                queue.append([dx, v])
                visited[dx] = visited[x] + 1

            if dx == 99:
                return visited[99]


if __name__ == '__main__':
    u, d = map(int, sys.stdin.readline().split())

    graph = [0 for _ in range(100)]

    for _ in range(u):
        x, v = map(int, sys.stdin.readline().split())
        graph[x-1] = v-1

    for _ in range(d):
        x, v = map(int, sys.stdin.readline().split())
        graph[x-1] = v-1
    print(bfs(graph))