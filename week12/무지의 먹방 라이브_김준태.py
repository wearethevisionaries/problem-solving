'''
문제 읽기 9:00

효율성 테스트에 부분 점수가 있다. -> 자료구조를 써야하나?

만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.

네크워크 장애가 K초 시점에 발생한다..

예시가 많이없어서 이해가 까다롭다

예전에 비슷한거 풀었는데 뭐지

리스트로 풀이 9:30
-효율성 다 못맞춤

한번 서칭 이후에 힙으로 푸는 걸 확인 -> 이코테에 있었다.

먹는데 시간이 적게 걸리는 음식부터 처리하면 순차적으로 먹는 과정을 빠르게 구현 가능하다.

자료구조보단 문제 푸는 방식이 어려운듯 (우선순위큐, 힙 둘다 가능)

문제 완료 10:15
'''

from collections import deque


def solution(food_times, k):
    if k >= sum(food_times):  # 모든 음식을 다 먹은경우
        return -1

    foods = deque(sorted(enumerate(food_times), key=lambda x: x[1]))  # 음식을 양 기준으로 우선순위 큐로 만들어 정렬
    total_food = 0  # 총 먹은 양
    last_food = 0  # 마지막으로 먹은 양

    while True:
        cur_food = (foods[0][1] - last_food) * len(foods)  # 이번 반복에서 먹을 음식 양

        if total_food + cur_food > k:  # 여태 먹은 양과 먹을 양의 합이 k가 넘어가면 k 시점의 음식을 구할 수 있다.
            break

        total_food += cur_food  # 총 먹은 양에 현재 먹은 양 더하기
        last_food = foods.popleft()[1]  # 다음 먹을 음식 세팅

    foods = sorted(foods, key=lambda x: x[0])  # 인덱스 기준 정렬

    cur_time = (k - total_food)  # 현재 시간
    return foods[cur_time % len(foods)][0] + 1  # 다음 음식의 인덱스는 현재 시간을 총 food의 길이로 나눈 나머지

