import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

dic = {}
i = -1

for v in sorted(data):
    if v not in dic:
        i += 1

    dic[v] = i

for j in data:
    sys.stdout.write(str(dic[j])+' ')