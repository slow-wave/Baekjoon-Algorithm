import sys
from collections import deque
import copy

def bfs(g, root, t):
    queue = deque([root])

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            x = dx[i] + a
            y = dy[i] + b

            if 0 > x or x >= n or 0 > y or y >= n or g[x][y] == 0:
                continue

            if g[x][y] == t:
                queue.append([x,y])
                g[x][y] = 0
    return 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    graph = []
    cnt, cnt1 = 0, 0

    for _ in range(n):
        row = list(sys.stdin.readline().rstrip())
        graph.append(row)
        
    graph1 = copy.deepcopy(graph)

    for a in range(n):
        for b in range(n):
            if graph1[a][b] == 'R':
                graph1[a][b] = 'G'

    for x in range(n):
        for y in range(n):
            t = graph[x][y]
            t1 = graph1[x][y]

            if t == 0:
                continue
            else:
                cnt += bfs(graph, [x, y], t)

            if t1 == 0:
                continue
            else:
                cnt1 += bfs(graph1, [x, y], t1)
    sys.stdout.write(str(cnt) + ' ' + str(cnt1))