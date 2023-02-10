#[1, 2, 3, 4, 5, 6] [7, 8, 9, 10, 11, 12] [6, 6]

def solution(lottos, win_nums):
    min_, max_ = 0,0
    match = len(list(set(lottos) & set(win_nums)))
    
    if match == 6:
        return [1,1]
    elif match == 0 and not lottos.count(0):
        return [6,6]
    else:
        if match == 0 or match == 1:
            min_ = 6
        else:
            min_ = 7-match
        max_ = 7-(lottos.count(0)+match)
        
        return [max_,min_]
    