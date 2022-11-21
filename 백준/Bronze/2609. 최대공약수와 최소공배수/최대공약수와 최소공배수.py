from sys import stdin

def solution(n1, n2):
    if n1 == 1 or n2 == 1:
        return [1, n1 * n2]

    end = n2 if n1 > n2 else n1

    for j in range(1, end+1):
        if n1 % j == 0 and n2 % j == 0:
            m = j
            n = j * n1 // j * n2 // j
    return [m, n]

if __name__ == '__main__':
    n1, n2 = map(int, stdin.readline().split())
    answer = solution(n1,n2)
    print(answer[0])
    print(answer[1])