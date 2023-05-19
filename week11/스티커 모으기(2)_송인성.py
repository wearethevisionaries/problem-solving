# 05.18 16:30~18:10 (미해결)

# 뜯은 양쪽 스티커는 사용할 수 없다.
    # 한칸 이상씩 건너뛰며 때야한다.
# 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 반환해야 한다.

# 아이디어
# 첫번째 것을 뜯어낼지 두번째 것을 뜯어낼지 결정한다.
# 2칸 건너뛴 것을 뜯을지, 3칸 건너뛴 것을 뜯을지 결정한다.


def solution(sticker):
    answer = 0
    # 길이가 1 이상이므로 1일 때는 바로 반환한다.
    if len(sticker) == 1: return sticker
    # 원형으로 만들어준다.
    round_sticker = 2 * sticker
    first_num = max(round_sticker)
    idx = round_sticker.index(first_num)
    pop_list = [first_num]
    # 최댓값을 기준으로 2칸 혹은 3칸 띄우며 리스트에 값을 저장 한 뒤에 리스트의 합을 비교하려고 했다..

    # for i, s in enumerate(round_sticker[idx:]):
    #     best = 0
    #     for j in range(i, len(round_sticker[idx:])):
            ##### 2 칸 이상씩 건너뛰는 방법을 모르겠다.
        
    return answer


#################1차##################
# for1 
# 숫자 리스트에서 하나씩 읽으며 숫자를 뜯어 낸다.
    # 뜯어낸 숫자는 리스트에 저장 한다.
    # for2
    # 2칸 뛰며 남은 수 한다.
        # 저장된 리스트 안에 값을 합한 뒤에 best checking 후 리스트를 리셋하고 for1로 돌아간다.
# def jump_sum(sticker):
#     new_sticker = sticker + [sticker[0]]

#     pop_list = []
#     best = 0
#     for i in range(len(new_sticker)):
#         pop_list.append(new_sticker[i])
#         # 저장된 숫자로 부터 2칸씩 뛰며 저장 한다.
#         for j in range(i, len(new_sticker), 2):
#             if new_sticker[j] not in pop_list:
#                 pop_list.append(new_sticker[j])
#         # 저장한 숫자를 모두 더한다.
#         score = sum(pop_list)
#         # 최댓값이랑 비교 후 갱신 한다.
#         if score > best:
#             best = score
#         # 리스트를 리셋한다.
#         pop_list.clear()
#     return best
    

# def solution(sticker):
#     answer = 0
    
#     answer = jump_sum(sticker)

#     return answer