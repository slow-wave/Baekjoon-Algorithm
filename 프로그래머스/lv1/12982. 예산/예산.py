def solution(d, budget):
    cnt_d = 0

    if sum(d) == budget:
        cnt_d = len(d)
    else:
        d.sort()

        for i in d:
            budget -= i
            if budget < 0:
                break
            cnt_d += 1
    return cnt_d