# 06.16 13:20~
# 완전 탐색
# DFS 현재 점, 양의 수, 늑대의 수, 이동 가능한 점

def dfs(idx, sheep, wolf, possible):
    # 현재 정점의 info 값 확인한다.
    global g_info, answer, graph
    if g_info[idx] == 0:
        # 양일 경우 +1, 최대일 때 업데이트한다.
        sheep += 1
        answer = max(answer, sheep)
    else:
        wolf += 1
        
    if wolf >= sheep:
        return 
    
    possible.extend(graph[idx])
    for p in possible:
        dfs(p, sheep, wolf, [i for i in possible if i != p])
    
def solution(info, edges):
    global answer, g_info, visited, graph
    answer = 0
    g_info = info
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for a, b in edges:
        graph[a].append(b)
        
    
    dfs(0, 0, 0, [])
    return answer