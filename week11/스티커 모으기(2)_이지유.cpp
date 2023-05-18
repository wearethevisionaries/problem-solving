/*
 * 22:35 [START]
 * 23:00 [APPROACH] Backtracking
 * 23:18 [TLE] move return condition inside for loop
 * 23:23 [TLE] move answer update operation inside exit condition
 * 23:25 [TLE]
 * 23:35 [END]
 */

#include <iostream>
#include <vector>
using namespace std;

constexpr int MAX_N = 100000;

int dp[2][MAX_N + 10];

int solution(vector<int> sticker) {
    int answer = sticker[0];
    
    /*
     * Input.
     */
    int N = sticker.size();
    
    /*
     * Compute.
     */
    if (1 == N) {
        return answer;
    }
    
    dp[0][1] = sticker[1];
    dp[1][1] = dp[1][0] = sticker[0];

    if (2 < N) {
        for(int i = 0; 2 > i; ++i) {
            for (int j = 2, endj = N - 1; endj > j; ++j) {
                dp[i][j] = max(dp[i][j - 1], dp[i][j - 2] + sticker[j]);
            }
        }
        
        dp[0][N - 1] = max(dp[0][N - 2], dp[0][N - 3] + sticker[N - 1]);
    }
    
    /*
     * Output.
     */
    return answer = max(dp[0][N - 1], dp[1][N - 2]);
}