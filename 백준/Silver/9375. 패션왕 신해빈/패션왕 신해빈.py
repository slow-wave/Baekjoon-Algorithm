import sys

def solution(items):
    combi = 1

    for k in items:
        combi *= len(items[k]) + 1

    return combi - 1

if __name__ == '__main__':
    T = int(sys.stdin.readline())

    for _ in range(T):
        n = int(sys.stdin.readline())
        items = {}

        if n == 0:
            print(0)

        else:
            for _ in range(n):
                value, key = sys.stdin.readline().split()

                items[key] = items.get(key, []) + [value]
            print(solution(items))