#include <string>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;

int solution(vector<int> info, vector<vector<int>> edges) {
    int answer = 0;
    
    vector<int> graph[info.size()];
    
    for (int i = 0, endi = edges.size(); endi > i; ++i) {
        graph[edges[i][0]].emplace_back(edges[i][1]);
    }
    
    queue<tuple<int,int,int>> q;
    
    q.emplace(0, 0, 0);
    
    for (int node, sheeps, wolves; !q.empty(); ) {
        node = get<0>(q.front());
        sheeps = get<1>(q.front());
        wolves = get<2>(q.front());
        
        q.pop();
        
        if (info[node]) {
            
        }
    }
    
    return answer;
}