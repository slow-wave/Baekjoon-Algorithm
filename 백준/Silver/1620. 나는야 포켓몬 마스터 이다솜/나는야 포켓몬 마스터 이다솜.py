import sys
input = sys.stdin.readline

N, M = map(int, input().split())

p_dict = {}
p_name = []

for i in range(N):
    name = input().rstrip()
    p_dict[name] = i+1
    p_name.append(name)

for _ in range(M):
    p = input().rstrip()
    
    if p.isdigit():
        print(p_name[int(p)-1]) 
    else:        
        print(p_dict[p])