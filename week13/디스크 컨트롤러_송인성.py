# 전에 풀었음 2시간 소요
# 간단 방법 : 요청 들어온 순서대로 처리한다.
# A-C-B : 소요시간 많이 걸리는 작업부터 처리한다. -> 우선순위 
# 한번에 하나의 요청만 처리 가능하다.
from heapq import heappop, heappush
def solution(jobs):
    answer = 0
    # 우선순위 큐를 선언한다.
    heap = []
    start, end, i = -1, 0, 0
    tot_time = 0
    while i < len(jobs):
        # 전 작업의 요청 시점과 종료 시간 범위 사이에 처리 해야될 작업이 있는지 판단한다.
        for job in jobs:
            if start < job[0] and job[0] <= end:
                # 다음 작업의 요청 시점이 지금 작업의 끝난 시간 이하에 있으면 작업 소요 시간 기준으로 heap 에 추가한다.
                heappush(heap, (job[1], job[0]))
        # heap 안에 작업이 존재할 경우에 if문 아래의 프로세스를 진행한다.
        if heap:
            # 작업 소요 시간이 작은 것 부터 빼낸다.
            now = heappop(heap)
            # start 기준 시간을 지금 작업의 끝나는 시점으로 갱신한다.
            start = end
            # 끝나는 시점을 지금 작업 소요 시간을 더해 갱신 해준다.
            end += now[0]
            # 각 작업의 요청 시점(now[1]) 부터 종료 까지(end) 소요된 시간의 합을 더해준다.
            answer += end - now[1]
            # 하나의 작업이 끝난 횟수를 더해준다.
            i += 1
        # heap 이 비어있으면 종료 시점을 더해준다.
        else:
            end += 1
    return answer // len(jobs)
