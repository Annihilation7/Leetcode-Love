//
// Created by 马振宇 on 2020/4/22.
//

#include <vector>
using namespace std;


class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int record_p[26] = {0};
        for(auto c: p)
            record_p[c - 'a']++;

        int l = 0;
        int r = -1;
        vector<int> res;

        int record_s[26] = {0};
        while(l < s.size()){
            if(r + 1 < s.size())
                record_s[s[++r] - 'a']++;
            while(record_s[s[r] - 'a'] > record_p[s[r] - 'a']){
                record_s[s[l++] - 'a']--;
            } 

            if(r - l + 1 == p.size())
                res.push_back(l);
        }
        return res;
    }
};


int main(){
    Solution solution();
    solution.findAnagrams("cbaebabacd", "abc");
}

