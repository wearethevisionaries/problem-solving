/*
 * 21:48 [START]
 * 21:50 [APPROACH] Arithmetic
 * 22:30 [WA] fix ternary operator condition
 * 22:43 [AC]
 */

#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(int r1, int r2) {
    long long answer = 0;
    
    long long R1 = pow((long long int)r1, 2);
    long long R2 = pow((long long int)r2, 2);
    
    for (long long int i = 1; r2 >= i; ++i) {
        answer += floor(sqrt(R2 - pow(i, 2))) - ((r1 >= i) ? ceil(sqrt(R1 - pow(i, 2))) : 0) + 1;
    }
    
    return answer << 2;
}