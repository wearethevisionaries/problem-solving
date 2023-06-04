'''
문제 읽기 2:00

개구간이 뭐였더라 -> a < x < b

실수 범위에서도 요격 미사일을 발사 가능

미사일 수 최솟값? -> dp는 아닌 것 같고.. 그리디?

폭격 미사일을 정렬해서 최소 단위로 요격하자

문제 풀이 2:30
'''


def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])  # 폭격 미사일을 끝나는 순으로 정렬, 최대한 오래 기다렸다가 요격하는 것이 최소의 미사일 사용이 가능

    intercept = 0  # 현재 요격 미사일이 발사되는 시점

    for target in targets:
        if intercept <= target[0]:  # 현재의 미사일로 요격이 불가능 한 경우
            answer += 1
            intercept = target[1]  # 요격 미사일 발사시점 갱신

    return answer
