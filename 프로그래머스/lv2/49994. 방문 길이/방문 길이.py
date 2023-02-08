def solution(dirs):
    xy = [0,0]
    move = []
    for d in dirs:
        if d == 'U':
            dist = [0,1]
        elif d == 'D':
            dist = [0,-1]
        elif d == 'L':
            dist = [-1,0]
        elif d == 'R':
            dist = [1,0]
        
        x_m = xy[0] + dist[0]
        y_m = xy[1] + dist[1]
        
        if x_m > 5 or x_m < -5 or y_m > 5 or y_m < -5:
            continue
        
        v = "{0} {1} {2} {3}".format(xy[0], xy[1], x_m, y_m)
        v_r = "{0} {1} {2} {3}".format(x_m, y_m, xy[0], xy[1])
        if v not in move:
            move.append(v)
        if v_r not in move:
            move.append(v_r)
        
        xy[0] += dist[0]
        xy[1] += dist[1]
         
    return len(move)//2
