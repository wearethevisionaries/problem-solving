/*
 * 23:06 [START]
 * 23:10 [APPROACH] Arithmetic + Queue
 * 23:18 {WA} fix val computation logic
 * 23:21 [WA/WA] fix val data type
 * 23:24 [WA/WA] [APPROACH]
 * 23:37 [AC/TLE]
 * 00:06 [END]
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp (pair<long long int,int> p1, pair<long long int,int> p2) {
    return p1.second < p2.second;
}

int solution(vector<int> food_times, long long k) {
    int answer = -1;

    vector<pair<long long int,int>> v;
    
    for (int i = 0, endi = food_times.size(); endi > i; ++i) {
        v.emplace_back(food_times[i], i);
    }
    
    sort(v.begin(), v.end(), greater<pair<long long int,int>>());
    
    for (long long int prev = 0; !v.empty() && k >= (v.back().first - prev) * v.size(); ) {
        if (prev != v.back().first) {
            k -= (v.back().first - prev) * v.size();
            prev = v.back().first;
        }
        
        v.pop_back();
    }
    
    if (!v.empty()) {        
        sort(v.begin(), v.end(), cmp);
        
        answer = v[k % v.size()].second + 1;
    }
    
    return answer;
}