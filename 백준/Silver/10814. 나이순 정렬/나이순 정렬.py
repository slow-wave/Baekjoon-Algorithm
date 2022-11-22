from sys import stdin, stdout

n = int(stdin.readline())
a = []

for _ in range(n):
    a.append(stdin.readline().split())

a.sort(key = lambda x : int(x[0]))

for i, n in a:
    stdout.write("{} {}".format(i,n))
    stdout.write('\n')