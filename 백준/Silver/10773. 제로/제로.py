from sys import stdin

n = int(stdin.readline())
stack = []

for _ in range(n):
    k = int(stdin.readline())

    if k == 0:
        stack.pop()
    else:
        stack.append(k)
print(sum(stack))