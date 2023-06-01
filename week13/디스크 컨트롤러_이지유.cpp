/*
 * 10:54 [START]
 * 11:12 [APPROACH] Greedy
 * 11:21 [AC]
 */

#include <string>
#include <vector>
#include <functional>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    
    int tmp = 0;
    int jobs_cnt = jobs.size();
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_pq;
    
    sort(jobs.begin(), jobs.end(), greater<vector<int>>());
    
    while (!jobs.empty() || !min_pq.empty()) {
        while (!jobs.empty() && tmp >= jobs.back()[0]) {
            min_pq.emplace(jobs.back()[1], jobs.back()[0]);
            jobs.pop_back();
        }

        if (!min_pq.empty()) {
            tmp += min_pq.top().first;
            answer += tmp - min_pq.top().second;
            min_pq.pop();
        }
        else {
            tmp = jobs.back()[0];
        }
    }
    
    return answer / jobs_cnt;
}