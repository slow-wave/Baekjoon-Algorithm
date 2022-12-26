import sys
from collections import deque

def push_front(x):
    queue.appendleft(x)

def push_back(x):
    queue.append(x)

def pop_front():
    if queue:
        print(queue.popleft())
    else:
        print(-1)

def pop_back():
    if queue:
        print(queue.pop())
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    queue = deque([])

    for _ in range(n):
        cmd = sys.stdin.readline().rstrip().split()
        if len(cmd) == 2:
            x = cmd[1]

        if cmd[0] == 'push_front':
            push_front(x)
        elif cmd[0] == 'push_back':
            push_back(x)
        elif cmd[0] == 'pop_front':
            pop_front()
        elif cmd[0] == 'pop_back':
            pop_back()
        elif cmd[0] == 'size':
            size()
        elif cmd[0] == 'empty':
            empty()
        elif cmd[0] == 'front':
            front()
        elif cmd[0] == 'back':
            back()