# 00:00 - 문제 못풀어서 다른 사람 코드 보고 공부했는데 그때까지 써둔 주석이 날아감;


def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    deliverie = 0
    pickup = 0

    for i in range(n):
        deliverie += deliveries[i]
        pickup += pickups[i]

        while deliverie > 0 or pickup > 0:
            deliverie -= cap
            pickup -= cap
            answer += (n - i) * 2

    return answer
