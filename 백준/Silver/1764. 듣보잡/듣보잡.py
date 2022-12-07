import sys

a, b = map(int, sys.stdin.readline().split())
set_a, set_b = set(), set()

for _ in range(a):
    set_a.add(sys.stdin.readline().rstrip())

for _ in range(b):
    set_b.add(sys.stdin.readline().rstrip())

answer = list(set_a & set_b)
answer.sort()

print(len(answer))
print('\n'.join(answer))