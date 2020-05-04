

class Solution {
public:
    string longestPalindrome(string s) {
        // 中心扩展算法求解
        if(s.size() == 0)
            return "";

        int start = 0, end = 0;
        for(int i = 0; i < s.size() - 1; i++){
            int length1 = expand(s, i, i);
            int length2 = expand(s, i, i + 1);
            int len = max(length1, length2);
            if(len > end - start + 1){
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substr(start, end - start + 1);
    }

    int expand(const string& s, int left_idx, int right_idx){
        while(left_idx >= 0 && right_idx < s.size() && s[left_idx] == s[right_idx]){
            left_idx--;
            right_idx++;
        }
        return right_idx - left_idx + 1 - 2;  // 有效回文串的真正长度
    }


    string longestPalindrome_dp(string s){
        // dp求解，代码比较简单，为什么dp反而没有中心扩展快呢？这个方法要慢很多。。。
        if(s.size() == 0)
            return "";

        int start = 0, end = 0;
        int max_length = 1;
        vector<vector<bool>> dp(s.size(), vector<bool>(s.size(), false));

        for(int r = 1; r < s.size(); r++)
            for(int l = 0; l < r; l++){
                if(s[l] == s[r] && (r - l <= 2 || dp[l + 1][r - 1])){  // special case: bab, aa
                    dp[l][r] = true;
                    if(r - l + 1 > max_length){
                        max_length = r - l + 1;
                        start = l;
                        end = r;
                    }
                }
            }
        return s.substr(start, end - start + 1);
};