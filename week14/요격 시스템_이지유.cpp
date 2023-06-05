/*
 * 22:48 [START]
 * 22:52 [APPROACH] Sorting, Greedy
 * 22:58 {WA} 요격 미사일은 실수인 x 좌표에서도 발사할 수 있습니다.
 * 23:01 [WA] fix val initialization logic
 * 23:07 [AC]
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> targets) {
    int answer = 0;
    
    sort(targets.begin(), targets.end());
    
    for (int i = 0, endi = targets.size(), val = -1; endi > i; ++i) {
        if (val <= targets[i][0]) {
            ++answer;
            val = targets[i][1];
        }
        else if (val > targets[i][1]) {
            val = targets[i][1];
        }
    }
    
    return answer;
}