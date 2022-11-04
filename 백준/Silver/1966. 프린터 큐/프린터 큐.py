from collections import deque

n = int(input())

for _ in range(n):
    count = 0
    
    N,M = map(int,input().split())
    doc = input().split()
    doc = [(d,int(doc[d])) for d in range(N)]

    queue= deque(doc)

    while queue:
        max_ = max(queue,key = lambda x:x[1])[1]
        i,p = queue.popleft()
        
        if p == max_: 
            if i == M:
                print(count+1)
                break
            else: 
                count += 1
        else:
            queue.append((i,p)) 