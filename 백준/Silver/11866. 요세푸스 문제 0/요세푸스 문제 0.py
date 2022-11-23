from sys import stdin, stdout
from collections import deque

n, k = map(int, stdin.readline().split())
queue = deque([i for i in range(1, n+1)])
answer = []

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

stdout.write("<"+", ".join(str(i) for i in answer)+">")