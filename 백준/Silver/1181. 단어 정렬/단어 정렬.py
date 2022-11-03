import sys

words = []
n = int(sys.stdin.readline())

for i in range(n):
    words.append(sys.stdin.readline().strip())
words = list(set(words))

words.sort()
words.sort(key = len)

print(*words, sep = '\n')