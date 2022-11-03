import heapq

def solution(operations):
    min_hq = []
    max_hq = []
    heapq.heapify(min_hq)
    heapq.heapify(max_hq)

    for op in operations:
        c = op.split(' ')[0]
        n = int(op.split(' ')[1])
        #insert
        if c == 'I':
            heapq.heappush(min_hq,n)
            heapq.heappush(max_hq, (-n, n))
        #최소값 삭제
        elif c == 'D' and n == -1:
            if min_hq:
                heapq.heappop(min_hq)
                max_hq.pop()
        #최댓값 삭제
        else:
            if max_hq:
                heapq.heappop(max_hq)[1]
                min_hq.pop()

    return [max_hq[0][1],min_hq[0]] if min_hq and max_hq else [0,0]
