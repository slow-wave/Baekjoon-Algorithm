n = int(input())

def min_count(n):
    if n == 1:
        return 1
    
    i,sum = 0,1
    
    while sum < n:
        sum += 6*i
        i += 1

    return i
    
print(min_count(n))