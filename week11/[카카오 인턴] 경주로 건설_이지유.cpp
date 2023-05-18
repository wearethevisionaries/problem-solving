/*
 * 16:00 [START]
 * 16:03 [APPROACH] Backtracking
 * 16:17 [WA] set answer to INF
 * 16:19 [WA] fix corner cost
 * 16:24 [TLE]
 * 17:00 [END]
 */

#include <string>
#include <vector>

using namespace std;

constexpr int MAX_N = 25;
constexpr int INF = 1 << 30;
constexpr int dx[] = {-1, 1, 0, 0};
constexpr int dy[] = {0, 0, -1, 1};

int N;
int cost[MAX_N + 3][MAX_N + 3][4];

void go(int& answer, vector<vector<int>>& board, int x, int y, int dir, int candidate) {
    /*
     * Check exit condition.
     */
    if (y == x && N - 1 == x) {
        answer = candidate;
        
        return;
    }
    
    /*
     * Continue searching.
     */
    for (int d = 0, nx, ny, tmp; 4 > d; ++d) {
        nx = x + dx[d];
        ny = y + dy[d];
        
        if (0 <= nx && N > nx && 0 <= ny && N > ny && !board[nx][ny]) {
            /*
             * Update candidate cost.
             */
            tmp = candidate + 100;
            
            if (dir != d) {
                tmp += 500;
            }
            
            /*
             * Backtrack.
             */
            if (answer > tmp && cost[nx][ny][d] >= tmp) {
                cost[nx][ny][d] = tmp;

                board[nx][ny] = 1;
                
                go(answer, board, nx, ny, d, tmp);
            
                board[nx][ny] = 0;
            }
        }
    }
}

int solution(vector<vector<int>> board) {
    int answer = 1 << 30;
    
    /*
     * Input.
     */
    N = board.size();
    
    for (int i = 0; N > i; ++i) {
        for (int j = 0; N > j; ++j) {
            for (int d = 0; 4 > d; ++d) {
                cost[i][j][d] = INF;
            }
        }
    }
    
    /*
     * Compute.
     */
    for (int d = 0; 4 > d; ++d) {
        cost[0][0][d] = 0;
    }
    board[0][0] = 1;
    
    go(answer, board, 0, 0, 4, 0);
    
    /*
     * Output.
     */
    return answer - 500;
}