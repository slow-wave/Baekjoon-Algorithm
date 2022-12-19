import sys
from collections import deque


def bfs(q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    day = 0

    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]

            if 0 <= x < n and 0 <= y < m and graph[x][y] == 0:
                q.append([x, y])
                graph[x][y] = graph[a][b] + 1

    for i in graph:
        if 0 in i:
            return -1
        day = max(day, max(i))
    return day-1



if __name__ == '__main__':
    m, n = map(int, sys.stdin.readline().split())
    graph = []
    queue = deque([])

    for x in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        graph.append(row)
        for y in range(m):
            if graph[x][y] == 1:
                queue.append([x, y])

    print(bfs(queue))
