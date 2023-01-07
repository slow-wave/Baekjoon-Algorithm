import sys

A, B, V = map(int, sys.stdin.readline().split())
k = (V-B)/(A-B)
print(int(k) if k == int(k) else int(k)+1)
