import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    f = 1
    prev = False
    c = 0

    for i in range(1, N+1):
        f *= i

    for i in range(len(str(f))-1, -1, -1):
        if str(f)[i] == '0' and i == len(str(f))-1:
            prev = True

        if str(f)[i] == '0' and prev is True:
            prev = True
            c += 1
        else:
            prev = False
    print(c)