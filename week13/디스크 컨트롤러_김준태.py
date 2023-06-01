'''
문제 읽기 9:00

힙으로 풀어보자

우선순위를 두어 디스크를 읽으면 평균 시간이 감소하겠다

소요 시간을 기준으로 힙으로 정렬하여 가능한 작업을 우선 채우자

문제 완료 9:45
'''

import heapq


def solution(jobs):
    answer, now, cnt = 0, 0, 0  # now 는 현재 시간
    start = -1
    heap = []

    while cnt < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])  # 소요시간, 요청 시점 기준으로 heap을 만들기

        if len(heap) > 0:  # 처리할 작업이 있는 경우
            cur_job = heapq.heappop(heap)
            start = now
            now += cur_job[0]
            answer += now - cur_job[1]  # 작업 요청시간부터 종료시간까지의 시간 계산
            cnt += 1  # 처리한 작업 카운트
        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)  # 소수점 이하의 수는 버림
