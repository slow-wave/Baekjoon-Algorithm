import sys

def cut(x, y, n):
    global zero, one, ans

    num = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != arr[i][j]:
                ans += '('
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                ans += ')'
                return

    ans += str(num)
    if num == 1:
        one += 1
    else:
        zero += 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
    zero, one = 0, 0
    ans = ''

    cut(0, 0, n)
    print(ans)
