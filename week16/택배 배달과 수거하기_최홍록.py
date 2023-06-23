from math import ceil
def solution(cap, n, deliveries, pickups):
    answer = 0
    add1 = sum(deliveries)
    add2 = sum(pickups)
    maximum = max(add1, add2)
    dlist = [0 for i in range(ceil(maximum/cap))]
    plist = [0 for i in range(ceil(maximum/cap))]
    temp = 0
    for i in range(ceil(maximum/cap)):
        for j, v in reversed(list(enumerate(deliveries))):
            
            while deliveries[j] > 0 and temp < cap:
                deliveries[j] -= 1
                temp +=1
                dlist[i] = max(dlist[i], j+1)
            if cap == temp:
                temp = 0
                break
            if deliveries[-1] == 0:
                deliveries.pop()
        print(deliveries)
    temp=0
    for i in range(ceil(maximum/cap)):
        for j, v in reversed(list(enumerate(pickups))):
            while pickups[j] > 0 and temp < cap:
                pickups[j] -= 1
                temp +=1
                plist[i] = max(plist[i], j+1)
            if cap == temp:
                temp = 0
                break
            if pickups[-1] == 0:
                pickups.pop()
    result = []

    for i in range(len(dlist)):
        result.append(max(dlist[i], plist[i]))
    answer = sum(result)*2
    return answer

print(solution(4,5,[1,0,3,1,2], [0,3,0,4,0]))