#include <unordered_map>
#include <utility>


class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> need, window;
        for(auto c: t)
            need[c]++;

        int left = 0;
        int right = 0;
        int length = INT_MAX;
        int start = 0;
        int valid = 0;

        while(right < s.size()){
            char c = s[right++];
            if(need.count(c)){
                window[c]++;
                if(window[c] == need[c])
                    valid++;
            }
            while(valid == need.size()){
                // 更新res
                if(right - left < length){
                    length = right - left;
                    start = left;
                }

                char d = s[left++];
                if(need.count(d)){
                    if(window[d] == need[d])
                        valid--;
                    window[d]--;
                }
            }
        }
        return length == INT_MAX ? "" : s.substr(start, length);
    }
};