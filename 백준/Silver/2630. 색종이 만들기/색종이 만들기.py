import sys

def cut(x, y, n):
    global zero, one

    num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    if num == 0:
        zero += 1
    else:
        one += 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())

    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    zero, one = 0, 0

    cut(0, 0, n)

    print(zero)
    print(one)