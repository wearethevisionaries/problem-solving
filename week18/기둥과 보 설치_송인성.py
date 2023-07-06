#07.06 11:30~

# 설치, 삭제 할 때 가능한지 여부를 판별하면 되겠다.

# 가능여부 판별 함수 
def right(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        # 보
        if a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        # 삭제할 때
        if b == 0:
            answer.remove([x,y,a])
            if not right(answer):
                answer.append([x,y,a])
        # 설치할 때
        if b == 1:
            answer.append([x,y,a])
            if not right(answer):
                answer.remove([x,y,a])
    return sorted(answer)