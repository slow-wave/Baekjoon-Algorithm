import sys
from collections import deque


def bfs(tmp_graph, v):
    queue = deque(v)

    # tmp_graph = copy.deepcopy(graph)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append([nx, ny])

    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(cnt, answer)

def makewall(cnt):
    if cnt == 3:
        tmp_graph = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] != 0:
                    tmp_graph[i][j] = graph[i][j]
        bfs(tmp_graph, v)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makewall(cnt+1)
                graph[i][j] = 0


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    v = []

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 2:
                v.append([a, b])

    answer = 0
    makewall(0)
    print(answer)