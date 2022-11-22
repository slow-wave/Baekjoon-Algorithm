from sys import stdin, stdout

n = int(stdin.readline())

stack = []

for _ in range(n):
    c = stdin.readline().split()

    if c[0] == 'push':
        stack.append(c[1])

    elif c[0] == 'pop':
        if stack:
            print(stack[-1])
            stack = stack[:-1]
        else:
            print(-1)

    elif c[0] == 'size':
        print(len(stack))

    elif c[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)