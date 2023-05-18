'''
문제 읽기 10:00

DP 문제로 풀 수 있다.

스티커를 떼어내면 인접한 스티커를 사용할 수 없다
스티커를 떼는 시작점이 중요할 것 같다. -> 두가지 케이스

원형 스티커 모양이므로 리스트를 한번 순회하면 되겠다.

완료 10:40

후기 : 머릿속이 복잡한데 DP 풀려니까 죽을 맛이다. 이번엔 FOR 문을 하나로 합쳤다.
'''


def solution(sticker):
    if len(sticker) <= 3:  # 스티커를 하나만 뗄 수 있는 케이스
        return max(sticker)

    first_sticker = [0 for _ in range(len(sticker))]  # 첫 스티커를 가져가는 케이스
    second_sticker = [0 for _ in range(len(sticker))]  # 첫 스티커를 가져가지 않는 케이스

    first_sticker[0], first_sticker[1] = sticker[0], sticker[0]
    second_sticker[1] = sticker[1]

    for i in range(2, len(sticker)):
        first_sticker[i] = max(first_sticker[i - 1], first_sticker[i - 2] + sticker[i])
        second_sticker[i] = max(second_sticker[i - 1], second_sticker[i - 2] + sticker[i])

    return max(first_sticker[-2], second_sticker[-1])