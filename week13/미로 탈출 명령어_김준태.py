'''
문제 읽기 1:00

n,m 사이즈 격자 미로 탈출 문제

그림 유형으로 봤을때 bfs? or dfs?

같은 격자 2번이상 방문 가능 -> 방문 중복 가능

총 거리는 k 여야함 -> k를 채우면 탐색 중지

문자열 사전순으로 나와야한다..

조건으로 탈출 불가능 시 impossible

bfs로 풀 수 있을 것 같다 1:25

큐 무한반복을 막기위해 break를 걸어야겠다. 1:35

문제 정답은 맞춤 하지만 시간이 오래걸린다. 1:55

정답자들을 참고하여 edge case의 탈출문 작성 2:05

아 왜 이거 골랐지..
'''

from collections import deque


def solution(n, m, x, y, r, c, k):
    queue = deque([(x, y, "", 0)])
    direction = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    while queue:
        x, y, answer, step = queue.popleft()

        if (x, y) == (r, c):  # 현재 지점이 도착 지점인 경우
            if (k - step) % 2:  # 남은 step이 짝수가 아니라면 다시 돌아오지 못하므로 불가능
                return "impossible"
            if step == k:  # step 조건이 충족되고 도착했을 경우
                return answer

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx <= n and 0 < ny <= m:  # 격자 미로 범위 내 이동
                if abs(nx - r) + abs(ny - c) + step < k:  # 남은 이동거리와 현재 step을 더한 값이 k 보다 작을 때
                    queue.append((nx, ny, answer + direction[i], step + 1))  # 방향과 step을 더해준다.
                    break  # 문자열의 우선순위가 존재하므로 break

    return "impossible"  # 모든 반복이 끝나도 도착할 수 없을 때
