
# 05.10 18:33 ~ 20:00
# w -> u, v (균형) 균형 인덱스 체크한다.
def get_balance_index(w):
    cnt1, cnt2 = 0, 0
    # 문자열 w를 리스트로 변환 한다. 리스트 인덱싱 하기 위함이다.
    for i, l in enumerate(list(w)):
        if l == '(':
            cnt1 += 1
        elif l == ')':
            cnt2 += 1
        if cnt1 == cnt2:
            return i
            

# 올바른 괄호인지 체크 함수, 옳으면 True 반환한다.
def check_right(u):
    # check한 문자 저장한다.
    r_list = []
    for i in u:
        # r_list 가 비어 있으면 저장한다.
        if not r_list:
            r_list.append(i)
            continue
        # r_list 존재 시 진행한다.
        if r_list[0] == ')':
            return False
        elif r_list[-1] == '(' and i == ')':
            r_list.pop()
        else:
            r_list.append(i)
    return True


def solution(p):
    if p == '':
        return p
    # 균형 잡힌 두 문자열 u(분리 불가), v(빈 문자열 가능) 로 분리한다.
    idx = get_balance_index(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check_right(u):
        u += solution(v)
        return u
    else:
        # 빈 문자열에 '(' 붙인다.
        ans = '('
        # 재귀 실행한다.
        ans += solution(v)
        ans += ')'
        u = list(u[1:-1])
        # 새로 만든 list로 된 u를 index 로 살피며 바꾼다.
        for i in range(len(u)):
            if u[i] == '(': u[i] = ')'
            else : u[i] = '('
        # 리스트를 문자열로 변환 후 붙인다.
        ans += ''.join(u)
    return ans
