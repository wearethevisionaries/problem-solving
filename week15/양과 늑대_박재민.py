# 12:07 - 문제 풀다가 갑자기 생각나서 작성 DFS로 풀려고 하는중(DP일거 같기도)
# 17:27 - DFS 오랫만에 풀려니까 구현하는법이 잘 생각이 안남;
# 25:30 - DFS는 만들었는데 재귀로 DFS를 구현해야 하나 고민중
#       - 단순하게 뒤로 가면 된다고 생각했는데 경우의 수가 생각보다 많음 DP인가? 아니면 BFS?
# 30:00 - 인접 리스트로 구현하니까 안됐음, edge를 그대로 받아서 구현한 케이스가 많았다

def solution(info, edges):
    global answer
    answer = 0
    visit = {0}
    
    def dfs(sheep, wolf):
        global answer
        answer = max(answer, sheep)
        if sheep <= wolf: return 
        
        for p, c in edges:
            if p in visit and c not in visit:
                visit.add(c)
                if not info[c]: dfs(sheep + 1, wolf)
                else: dfs(sheep, wolf + 1)
                visit.remove(c)
    dfs(1, 0)
    return answer