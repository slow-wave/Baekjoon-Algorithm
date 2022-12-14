import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
sum_ = [0] * (len(arr)+1)
prev = 0

for i in range(len(arr)):
    prev += arr[i]
    sum_[i+1] = prev

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())

    sys.stdout.write(str(sum_[e] - sum_[s-1])+'\n')