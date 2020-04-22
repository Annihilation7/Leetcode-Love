//
// Created by 马振宇 on 2020/4/22.
// 滑动窗口的题，需要在滑动窗口内做一些简单的记录
//

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int freq[256] = {0};  // record，比哈希表好很多
        int l = 0;
        int r = -1;
        int max_length = 0;

        while(l < s.size()){
            if(r + 1 < s.size() && freq[s[r + 1]] == 0)
                freq[s[++r]]++;
            else
                freq[s[l++]]--;

            max_length = max(max_length, r - l + 1);
        }
        return max_length;
    }
};