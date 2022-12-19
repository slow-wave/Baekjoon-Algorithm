import sys
from collections import deque


def bfs(q):
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    day = 0

    while q:
        a, b, c = q.popleft()
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]

            if 0 <= x < h and 0 <= y < n and 0 <= z < m and graph[x][y][z] == 0:
                q.append([x, y, z])
                graph[x][y][z] = graph[a][b][c] + 1

    for i in graph:
        for j in i:
            for k in j:
                if k ==0:
                    return -1
                    exit(0)
            day = max(day, max(j))
    return day-1


if __name__ == '__main__':
    m, n, h = map(int, sys.stdin.readline().split())
    graph = []
    queue = deque([])

    for x_ in range(h):
        tmp = []
        for y_ in range(n):
            tmp.append(list(map(int, sys.stdin.readline().split())))
            for k in range(m):
                if tmp[y_][k] == 1:
                    queue.append([x_, y_, k])
        graph.append(tmp)

    print(bfs(queue))