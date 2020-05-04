class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> record;
        int res = 0;

        for(auto c: s)
            record[c]++;

        for(auto c: record)
            res += c.second / 2 * 2;

        return res == s.size() ? res : res + 1;
    }
};