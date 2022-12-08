import sys

n, k = map(int, sys.stdin.readline().split())
money = []
remain = k
cnt = 0

for _ in range(n):
    v = int(sys.stdin.readline())
    if k >= v:
        money.append(v)
money.sort(reverse= True)

for m in money:
    if remain == 0:
        break

    if remain >= m:
        cnt += remain//m
        remain = k % m
    else:
        pass

print(cnt)