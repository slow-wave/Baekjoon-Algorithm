import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

# 0층부터 256층까지 반복
for target in range(257):
    plus, minus = 0, 0

    for i in range(n):
        for j in range(m):

            # 블록이 층 수보다 크거나 같으면 -> 추가
            if graph[i][j] >= target:
                plus += graph[i][j] - target

            # 블록이 층 수보다 작으면 -> 삭제
            else:
                minus += target - graph[i][j]
    #인벤토에 있는 블록 수 범위 안에서 추가, 삭제 되었다면
    if plus + b >= minus:
        # 최저 시간이면
        if minus + (plus * 2) <= answer:
            answer = minus + (plus * 2)
            idx = target

print(answer, idx)