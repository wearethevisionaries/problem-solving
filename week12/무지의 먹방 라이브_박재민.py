# 01:30 - 문제 다 읽음
# 02:00 - 효율성 테스트 있는거 보니까 그냥 큐로 하면 무조건 걸릴듯
# 07:14 - food_times 길이로 k를 나누고 몫이 0 일때부터 시작하면 될거같다
# 10:11 - 이러면 값이 0일때 처리가 안되더라
# 12:41 - 이게 그리디라고? 왜지
# 14:32 - 그냥 큐라도 써보자
# 20:00 - 큐 쓰니까 정확성은 통과한다 근데 역시나 효율성은 못통과한다
# 30:00 - GG
# -------------------
# 35:00 - heap으로 정렬해서 풀어도 되는구나
# 37:00 - 다른 사람들은 heap으로 한바퀴를 돌수있을때까지 돌았다(이부분이 핵심이었다)
# 45:00 - 답은 나옴

from heapq import heappush, heappop


def solution(food_times, k):
    # 방송이 멈추기 전에 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return -1

    # time을 기준으로 정렬하는 heap에 넣어준다
    heap = []
    food_len = len(food_times)
    for idx, time in enumerate(food_times):
        heappush(heap, (time, idx + 1))

    # 핵심 코드, 현재 음식을 다 먹는 시간 * 음식 수가 k보다 작으면 들어간다
    time = 0
    while (heap[0][0] - time) * food_len < k:
        k -= (heap[0][0] - time) * food_len
        time += heap[0][0] - time
        food_len -= 1
        heappop(heap)

    # 원래는 인덱스 순서로 정렬돼있었으니까 다시 돌려준다
    heap = sorted(heap, key=lambda x: x[1])
    return heap[k % food_len][1]


# 정확성만 통과하는 코드
# from collections import deque

# def solution(food_times, k):
#     queue = deque([(idx + 1, time) for idx, time in enumerate(food_times)])
#     for _ in range(k):
#         if queue:
#             idx, time = queue.popleft()
#             if time - 1 != 0:
#                 queue.append((idx, time - 1))
#         else:
#             return -1
#     return queue.popleft()[0] if queue else -1
