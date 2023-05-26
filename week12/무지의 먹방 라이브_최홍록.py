def solution(food_times, k):
    j=-1
    print([1,2,3]-[1,1,1])
    if sum(food_times)<=k:
        return -1
    leng=len(food_times)
    if leng>k:
        return k+1
    for i in range(k):
        j=(j+1)%leng
        while food_times[j]==0:
            j=(j+1)%leng
        food_times[j]-=1
    j=(j+1)%leng
    for i in range (leng):
        if food_times[j]==0:
            j=(j+1)%leng
        else:
            return j%leng+1

