'''
문제 읽기 9:50

문제 이해가 좀 어렵다. 지문이 길다..

매개변수 설명 확인 10:00

# TODO
빈 문자열 일 경우 return, 올바른 괄호 문자열이면 return
10:15

# TODO
균형잡힌 괄호 문자열을 확인
10:05

# TODO
올바른 괄호 문자열을 확인
10:15

# TODO
재귀 호출이 이뤄짐
10:25

완료 10:30

후기 : 아직 주석처리가 익숙치 않다. 오랜만에 프로그래머스를 쓰니 디버깅이 오래 걸린다. 좀 더 간결하게 가능할 것 같다.

'''


def is_balanced(word):  # 균형잡힌 괄호 문자열 확인
    if word.count('(') == word.count(')'):
        return True
    return False


def is_correct(word):  # 올바른 괄호 문자열 확인
    stack = []
    for w in word:
        if w == '(':
            stack.append(w)
        else:  # ) 가 입력됐을 경우
            if not stack:  # stack이 비어있다면 잘못된 문자열
                return False
            elif stack[-1] == '(':  # 마지막 문자열이 ( 라면 괄호 짝 제거
                stack.pop()

    if stack:  # 모든 stack이 비어있어야 올바른 괄호 문자열
        return False
    return True


def separate(word):  # u,v 분리
    for i in range(2, len(word) + 1, 2):  # u,v 분리, u는 더 이상 균형잡힌 괄호 문자열로 분리할 수 없다.
        if is_balanced(word[:i]):
            u, v = word[:i], word[i:]
            break
    return u, v


def solution(p):
    answer = ''

    if p == '' or is_correct(p):  # 1번
        return p

    u, v = separate(p)  # 2번

    if is_correct(u):  # 3번
        answer += u + solution(v)  # 3-1번

    else:  # 4번
        answer += '(' + solution(v) + ')'  # 4-1 ~ 4-3번
        for w in u[1:-1]:  # 4-4번
            if w == '(':
                answer += ')'
            else:
                answer += '('

    return answer
