# 06.09 08:30~

# 최소 사용 필요하다.
# 2차원 공간이다.
# A : x축 평행 구간 (s,e)로 표시
# B : y축 평행, x좌표에 걸쳐있는 모든 폭격 미사일을 관통 가능 s,e 불포함

def solution(targets):
    # 조건 범위 최댓값 + 1 까지 포함한다.
    answer, defense = 0, 100000001
    # 요격 위치 defense 갱신하며 이동한다.
    for start, end in sorted(targets, reverse=True):
        # end와 defense가 같으면 폭발하지 않는다.
        if end <= defense:
            defense = start + 0.5
            answer += 1
    return answer