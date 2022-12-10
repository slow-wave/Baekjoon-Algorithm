import sys
from collections import deque

def bfs(graph):
    queue = deque([1])
    visited = [0 for _ in range(node + 1)]
    cnt = 0

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

if __name__ == '__main__':
    node = int(sys.stdin.readline())
    edge = int(sys.stdin.readline())

    graph = [[] for _ in range(node + 1)]

    for _ in range(edge):
        n1, n2 = map(int, sys.stdin.readline().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    print(bfs(graph)-1)