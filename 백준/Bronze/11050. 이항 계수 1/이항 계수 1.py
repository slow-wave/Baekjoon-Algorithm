import math
from sys import stdin, stdout

N, K = map(int, stdin.readline().split())
stdout.write(str(math.factorial(N) // (math.factorial(K)*math.factorial(N-K))))