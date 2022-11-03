import heapq

def solution(scoville,K):
    mix = 0
    
    hq = scoville
    
    heapq.heapify(hq)

    while(hq[0] < K and len(hq) != 1):
        heapq.heappush(hq,heapq.heappop(hq) + (heapq.heappop(hq)*2))
        mix += 1
    
    if hq[0] < K:
        return -1
    else:    
        return mix