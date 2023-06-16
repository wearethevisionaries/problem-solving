#include <string>
#include <vector>

using namespace std;

constexpr int MAX_N = 1000;
constexpr int MAX_M = 1000;
constexpr int ENEMY = 1;
constexpr int ALLY = 2;

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    
    int filter[MAX_N + 1][MAX_M + 1] = {0};
    int N = int(board.size());
    int M = int(board[0].size());
    int skill_cnt = int(skill.size());
    int r1, c1, r2, c2;
    
    for (int i = 0; skill_cnt > i; ++i) {
        r1 = skill[i][1];
        c1 = skill[i][2];
        r2 = skill[i][3] + 1;
        c2 = skill[i][4] + 1;
        
        switch(skill[i][0]) {
            case ENEMY:
                filter[r1][c1] -= skill[i][5];
                filter[r2][c2] -= skill[i][5];
                filter[r1][c2] += skill[i][5];
                filter[r2][c1] += skill[i][5];
                break;
            case ALLY:
                filter[r1][c1] += skill[i][5];
                filter[r2][c2] += skill[i][5];
                filter[r1][c2] -= skill[i][5];
                filter[r2][c1] -= skill[i][5];
                break;
            default:
                break;
        }
    }
    
    for (int i = 0; N > i; ++i) {
        for (int j = 1; M > j; ++j) {
            filter[i][j] += filter[i][j - 1];
        }
    }
    for (int i = 1; N > i; ++i) {
        for (int j = 0; M > j; ++j) {
            filter[i][j] += filter[i - 1][j];
        }
    }
    
    for (int i = 0; N > i; ++i) {
        for (int j = 0; M > j; ++j) {
            if (0 < (board[i][j] + filter[i][j])) {
                ++answer;
            }
        }
    }
    
    return answer;
}