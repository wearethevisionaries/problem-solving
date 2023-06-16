'''
문제 읽기 2:00

이진트리 노드 순회 문제

조건을 상정하여 방문 -> dfs 풀이?

dfs 구현 test case가 몇개 틀린다.. 2:40

인터넷 풀이 참고 후 제출

생각보다 풀이가 간단하다.
'''


def dfs(sheep, wolf, answer, info, edges, visited):
    if sheep <= wolf:  # 양이 모두 잡아먹히는 경우 return
        return
    else:
        answer.append(sheep)

    for i, j in edges:
        if visited[i] and not visited[j]:  # 방문 한 노드와 연결된 노드 탐색
            visited[j] = 1  # 방문처리
            if info[j] == 1:  # 방문하려는 노드가 늑대인 경우
                dfs(sheep, wolf + 1, answer, info, edges, visited)
            else:  # 방문하려는 노드가 양인 경우
                dfs(sheep + 1, wolf, answer, info, edges, visited)
            visited[j] = 0  # 재 방문이 가능하게 만들어준다. (모든 경우의 수 탐색을 위함)


def solution(info, edges):
    answer = []
    visited = [0 for _ in range(len(info))]  # 방문 리스트
    visited[0] = 1  # 루트 노드 방문처리

    dfs(1, 0, answer, info, edges, visited)  # 양을 한마리 가진채로 dfs 시작
    return max(answer)  # 모든 경우의 수 중 최대 양 값 출력
