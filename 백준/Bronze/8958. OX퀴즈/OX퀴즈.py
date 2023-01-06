import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    problem = list(sys.stdin.readline().rstrip())
    result = 0
    prev = 0
    add = 1

    for p in problem:
        if p == 'X':
            prev = 0
            add = 1
            continue

        if prev == 1:
            add += 1

        result += add
        prev = 1

    print(result)