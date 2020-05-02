
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0)
            return 0;

        unordered_map<char, int> record;
        int l = 0, r = 0;  // 左闭右开
        int res = 0;

        while(r < s.size()){
            char c = s[r++];  // 在里面加了，所以 <size()是没问题的，最后会让r==s.size()
            record[c]++;

            while(record[c] > 1){
                record[s[l++]]--;
            }

            res = max(res, r - l);
        }
        return res;
    }
};