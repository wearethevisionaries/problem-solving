# 01:21 - 문제 다 읽음(이거 수업시간에 거의 같은 문제를 봤었는데 기억이 안난다)
# 05:24 - 일단 정렬이 필요할 것 같음
#       - 1. 끝을 기준으로 정렬
# 07:50 - 마지막 값 중에 가장 작은 값이 다음 값의 사이에 들어가는지 확인하면 될거 같음
# 19:50 - 정확도 45%, 접근 자체는 맞는거 같은데 if문을 어떻게 해야할지 감이 잘 안잡힘
# 23:55 - if문을 start만 보는걸로 해결
# 24:00 - 끝


def solution(targets):
    sorted_targets = sorted(targets, key=lambda x: x[1])
    answer, min_end = 1, sorted_targets[0][1]
    for length in sorted_targets[1:]:
        start, end = tuple(length)
        if not (start < min_end):
            min_end = end
            answer += 1
    return answer
