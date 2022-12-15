import sys

def cut(x, y, n):
    global minus, zero, one

    num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                cut(x, y, n//3)
                cut(x, y+n//3, n//3)
                cut(x, y+n//3*2, n//3)

                cut(x+n//3, y, n//3)
                cut(x+n//3, y+n//3, n//3)
                cut(x+n//3, y+n//3*2, n//3)

                cut(x+n//3*2, y, n//3)
                cut(x+n//3*2, y+n//3, n//3)
                cut(x+n//3*2, y+n//3*2, n//3)
                return

    if num == -1:
        minus += 1
    elif num == 0:
        zero += 1
    else:
        one += 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    minus, zero, one = 0, 0, 0

    cut(0, 0, n)
    print("{}\n{}\n{}".format(minus, zero, one))