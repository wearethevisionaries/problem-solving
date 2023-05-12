/*
 * 19:23 [START]
 * 19:32 Recursion(Divide and Conquer)
 * 20:11 [AC]
 */

#include <string>
#include <vector>

using namespace std;

string go(string& p) {    
    /*
     * Step 1.
     */
    if ("" == p) {
        return p;
    }
    
    /*
     * Step 2.
     */
    int npos = 1;
    
    for (int is_valid = ('(' == p[0]) ? -1 : 1, endnpos = p.size(); endnpos > npos && is_valid; ++npos) {
        is_valid += ('(' == p[npos]) ? -1 : 1;
    }
    
    string u = p.substr(0, npos);
    string v = p.substr(npos, p.size() - npos);
    
    vector<int> stack;
    
    for (int i = 0, endi = u.size(); endi > i; ++i) {
        if (')' == u[i] && !stack.empty() && '(' == stack.back()) {
            stack.pop_back();
        }
        else {
            stack.emplace_back(u[i]);
        }
    }
    
    /*
     * Step 3.
     */
    if (stack.empty()) {
        return u + go(v);
    }
    
    /*
     * Step 4.
     */
    v = "(" + go(v) + ")";
    
    for (int i = 1, endi = u.size() - 1; endi > i; ++i) {
        v.append('(' == u[i] ? ")" : "(");
    }
    
    return v;
}

string solution(string p) {
    string answer = "";
    
    answer = go(p);
    
    return answer;
}