/*
 * 11:33 [START]
 * 11:39 [APPROACH] Casework
 * 12:33 [END]
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    
    k -= abs(x - r) + abs(y - c);
    
    if ((0 > k) || (k & 1)) {
        return answer = "impossible";
    }
    
    int val1 = 0, val2 = 0;
    
    /*
     * Step 1: 'd'
     */
    if (r > x) {
        answer.append(r - x, 'd');
        val1 = min(k / 2, n - r);
    }
    else {
        val1 = min(k / 2, n - x);
    }
    
    if (0 < val1) {
        answer.append(val1, 'd');
        k -= val1 << 1;
    }
    
    /*
     * Step 2: 'l'
     */
    if (c < y) {
        answer.append(y - c, 'l');
        val2 = min(k / 2, c - 1);
    }
    else {
        val2 = min(k / 2, y - 1);
    }
    
    if (0 < val2) {
        answer.append(val2, 'l');
        k -= val2 << 1;
    }
    
    /*
     * Step 3: 'rl'
     */
    for (; 0 < k; k -= 2) {
        answer.append("rl");
    }
    
    /*
     * Step 4: 'r'
     */
    if (c > y) {
        answer.append(c - y, 'r');
    }
    
    answer.append(val2, 'r');
    
    /*
     * Step 5: 'u'
     */
    if (r < x) {
        answer.append(x - r, 'u');
    }
    
    answer.append(val1, 'u');
    
    return answer;
}