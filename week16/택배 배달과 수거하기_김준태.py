'''
문제 읽기 9:00

최소 이동거리 구하기. -> 그리디

그냥 구현으로 풀면 시간초과 걸릴듯

문제 완료 10:15
'''

def solution(cap, n, deliveries, pickups):
    answer = 0

    n_deliver = 0
    n_pick = 0


    for i in range(1, n + 1):
        # 가장 먼 집부터 배달/수거 시작
        n_deliver += deliveries[-i]
        n_pick += pickups[-i]

        # 물류창고를 다시 가야하는 위치 찾기
        while n_deliver > 0 or n_pick > 0:
            n_deliver -= cap
            n_pick -= cap

            # 왕복 거리 계산
            answer += (n - i + 1) * 2

    return answer