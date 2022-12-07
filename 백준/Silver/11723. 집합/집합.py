import sys


def add(x):
    if x not in s:
        s.add(x)


def remove(x):
    if x in s:
        s.remove(x)


def check(x):
    if x in s:
        return 1
    else:
        return 0


def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.add(x)


def all_():
    return set(list(range(1, 21)))


def empty():
    return set()


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    s = set()

    for _ in range(n):
        cmd = sys.stdin.readline().split()

        if cmd[0] == 'add':
            add(int(cmd[1]))

        elif cmd[0] == 'remove':
            remove(int(cmd[1]))

        elif cmd[0] == 'check':
            print(check(int(cmd[1])))

        elif cmd[0] == 'toggle':
            toggle(int(cmd[1]))

        elif cmd[0] == 'all':
            s = all_()

        elif cmd[0] == 'empty':
            s = empty()