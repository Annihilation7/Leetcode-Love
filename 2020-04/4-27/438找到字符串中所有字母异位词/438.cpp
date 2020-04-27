

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int record_p[26] = {0};
        for(auto c: p)
            record_p[c - 'a']++;

        int record_s[26] = {0};
        vector<int> res;
        int left = 0;
        int right = -1;  // 滑动窗口初始化为空，左闭右闭区间

        while(left < s.size()){
            if(right + 1 < s.size())
                record_s[s[++right] - 'a']++;
            while(record_s[s[right] - 'a'] > record_p[s[right] - 'a'])
                record_s[s[left++] - 'a']--;

            if(right - left + 1 == p.size())
                res.push_back(left);

            if(right == s.size() - 1)  // abab, ab测试样例 最后退出循环的条件，真的太关键了！好题！
                break;
        }
        return res;
    }
};