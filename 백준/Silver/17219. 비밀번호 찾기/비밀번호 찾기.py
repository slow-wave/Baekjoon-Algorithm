import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}

for _ in range(n):
    domain, pwd = sys.stdin.readline().split()
    dic[domain] = pwd

for _ in range(m):
    sys.stdout.write(dic[sys.stdin.readline().rstrip()] + '\n')