#07.07 12:03~

# 참고했다.

def solution(n, a_scores):
    def getscore(r_scores):
        tot = 0
        for i in range(len(a_scores)):
            if a_scores[i] < r_scores[i]:
                tot += 10 - i
            elif a_scores[i] > 0:
                tot -= 10 - i
        return tot

    def recursive(idx, left, r_scores):
        nonlocal answer, max_score
        if idx == -1 and left:
            return
        if left == 0:
            score = getscore(r_scores)
            if max_score < score:
                answer = r_scores.copy()
                max_score = score
            return
        for i in range(left, -1, -1):
            r_scores[idx] = i
            recursive(idx - 1, left - i, r_scores)
            r_scores[idx] = 0

    max_score = 0
    answer = [0 for _ in range(11)]
    recursive(10, n, [0 for _ in range(11)])
    return [-1] if max_score == 0 else answer