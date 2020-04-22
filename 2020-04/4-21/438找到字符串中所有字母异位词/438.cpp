//
// Created by 马振宇 on 2020/4/22.
//

#include <vector>

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        record_p = get_record(p);
        int record_s[26] = {0};
        int l = 0;
        int r = -1;
        vector<int> res;

        while(l < s.size()){
            if(r + 1 < s.size() && record_s[s[r + 1]] < record_p[s[r + 1]])
                record_s[s[++r]]++;
            else

        }
    }

    int* get_record(const string& p){
        int record[26] = {0};
        for(const auto& c: p)
            record[c]++;
        return record;
    }
};

