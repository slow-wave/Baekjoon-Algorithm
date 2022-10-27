import sys
input = sys.stdin.readline

n = int(input())
room = []
c = 0

for i in range(n):
    room.append(tuple(map(int,input().split())))

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

target = room[0][1]

for i in range(1,len(room)):
    if room[i][0] >= target:
        c += 1
        target = room[i][1]

print(c+1)