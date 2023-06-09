import math

def solution(r1, r2):
    answer = 0
    max_len = max(r1,r2)
    min_len = min(r1,r2)
    for i in range(max_len+1):

        temp_max = max_len**2 - i**2
        temp_min = max(min_len**2-i**2,0) 
        if temp_max>=temp_min:
            answer += abs(int(int(math.sqrt(temp_max)) - rev_gauss(math.sqrt(temp_min)))+1)
    answer = answer*4 - 4*(max_len-min_len+1)
    return answer

def rev_gauss(i):
    if float(i).is_integer():
        return i
    else:
        return int(i)+1