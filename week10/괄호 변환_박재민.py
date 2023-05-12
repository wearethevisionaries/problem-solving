def check(p):
    stack = []
    for c in p:
        if c == "(":
            stack.append("(")
        if c == ")":
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()
    return True if not stack else False


def sep(p):
    count1, count2 = 0, 0
    u, v = "", ""
    for i, c in enumerate(p):
        if c == "(":
            count1 += 1
        if c == ")":
            count2 += 1
        if count1 == count2:
            u = p[: i + 1]
            v = p[i + 1 :]
            break
    return u, v


def change(p):
    if p == "":
        return ""
    u, v = sep(p)
    if check(u):
        return u + change(v)
    else:
        temp = "(" + change(v) + ")"
        temp += "".join([")" if c == "(" else "(" for c in u[1:-1]])
        return temp


def solution(p):
    return p if check(p) else change(p)
