# 05.26 풀었던 문제지만 다시 푼다.

# 효율성 테스트 heappush & heappop -> O(logN)
# 1초 동안만 섭취한다. -> 이후 다음 음식 섭취
# 회전판 이동 시간 없다.

# 시작한 지 K초 후 중단한다. -> 다음 섭취해야 하는 음식 찾는다.
# 몇번 음식부터 다시 섭취하면 되나? -> 음식 번호 중요하다.
    # enumerate

# 효율성.. 정답.. 다 놓쳤다. 45분정도
# def solution(food_times, k):
#     answer = 0
#     i = 0
#     while k > 0:
#         if sum(food_times) <= k: return -1
        
#         # 인덱스 기준으로 음식을 하나씩 뺀다.
#         if food_times[i] != 0:
#             food_times[i] -= 1
#             k -= 1
#             i += 1

#         else:
#             i += 1
#             continue
#         # 인덱스가 food_times 길이를 초과하면 리셋 해준다.
#         if i == len(food_times): i = 0
    
#     return i + 1
    

# 정답 참조 
from heapq import heappush, heappop
def solution(food_times, k):
    if sum(food_times) <= k: return -1
    
    q = []
    # 1번부터 음식 시작한다. start=1
    for i, f in enumerate(food_times, start=1):
        # 음식 양을 기준으로 우선 순위로 우선순위 큐 삽입한다.
        heappush(q, (f, i))
        
    # 먹은 음식양의 합을 매번 계산하지 않게 새로운 변수 선언한다.
    sum_food = 0
    
    # 전에 먹던 음식의 양을 저장한다.
    previous = 0
    
    # 길이를 while loop 에서 매번 구하는 것보다 한번 구해 놓고 음식을 다 먹을 때마다 빼는것이 효율적이다.
    length = len(food_times)
    
    # 지금 먹을 음식의 양과 기존까지 먹은 음식의 양의 합이 k 보다 작거나 같으면 종료한다.
    while sum_food + ((q[0][0] - previous) * length) <= k: 
        # 우선순위 큐에서 양이 가장 적은 음식을 먼저 먹는다.
        now, i = heappop(q)
        
        sum_food += (now - previous) * length
        length -= 1
        # 지금 먹었던 음식의 양을 기존 먹은 음식의 양 변수에 저장한다.
        previous = now
    # 남은 음식을 인덱스 기준으로 정렬한다.
    answer = sorted(q, key = lambda x:x[1])
    # 현재의 시간을 총 food_times 길이로 나눈 나머지로 인덱스를 반환한다.
    return answer[(k - sum_food) % length][1]
        