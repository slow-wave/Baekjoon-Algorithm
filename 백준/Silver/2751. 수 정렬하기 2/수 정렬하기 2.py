from sys import stdin

n = int(stdin.readline())
array = []

for _ in range(n):
    array.append(int(stdin.readline()))
array.sort()

print('\n'.join(str(i) for i in array))