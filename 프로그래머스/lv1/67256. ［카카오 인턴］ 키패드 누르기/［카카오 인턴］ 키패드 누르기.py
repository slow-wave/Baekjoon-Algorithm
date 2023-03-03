def solution(numbers, hand):
    answer = ''
    L, R = '*', '#'
    loc = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), '#':(3,2), 0:(3,1)}
    
    for n in numbers:
        if n in (1,4,7):
            answer += 'L'
            L = n
        elif n in (3,6,9):
            answer += 'R'
            R = n
        else:
            #거리구하기
            distL = abs(loc[L][0]-loc[n][0]) + abs(loc[L][1]-loc[n][1])
            distR = abs(loc[R][0]-loc[n][0]) + abs(loc[R][1]-loc[n][1])
            #거리가 같다면 무슨 손 잡이인지에 따라 결정
            if distL == distR:
                if hand == 'right':
                    answer += 'R'
                    R = n
                else:
                    answer += 'L'
                    L = n
            #아니라면 거리가 짧은 곳으로 이동
            else:
                if distL > distR:
                    answer += 'R'
                    R = n
                else:
                    answer += 'L'
                    L = n
    return answer
