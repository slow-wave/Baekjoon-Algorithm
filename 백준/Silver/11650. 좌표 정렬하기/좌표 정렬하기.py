from sys import stdin, stdout

n = int(stdin.readline())
xy = []

for _ in range(n):
    xy.append(list(map(int, stdin.readline().split())))

xy.sort()

stdout.write("\n".join(str(i[0]) + ' ' + str(i[1]) for i in xy))