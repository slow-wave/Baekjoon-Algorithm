import sys

n = int(sys.stdin.readline())
p_l = list(map(int, sys.stdin.readline().split()))

p_l.sort()
s = 0

for i in range(n):
    s += p_l[i] * (n-i)

print(s)