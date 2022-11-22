from sys import stdin

n = int(stdin.readline())
min = float("inf")

for i in range(n//3 + 1):
    b = n - (3 * i)

    if b % 5 == 0:
        c = b // 5 + i

        if min > c:
            min = c

if min == float("inf"):
    print(-1)
else:
    print(min)