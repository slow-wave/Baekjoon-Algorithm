from sys import stdin

while(True):
    stack = []

    s = stdin.readline().rstrip()

    if s == '.':
        break

    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(c)

    if stack:
        print('no')
    else:
        print('yes')