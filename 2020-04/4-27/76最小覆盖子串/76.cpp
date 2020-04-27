#include <unordered_map>
#include <utility>


class Solution {
public:
    string minWindow(string s, string t) {  // 一道滑动窗口的题
        unordered_map<char, int> record_t = get_record(t);
        unordered_map<char, int> record_s;
        string res = s + "#";  // 初始化比s的长度还要大1,所以肯定是可以更新s的
        int left = 0;
        int right = -1;

        while(left < s.size()){
            if(right + 1 < s.size() && !is_equal(record_s, record_t)){
                record_s[s[++right]]++;
            }
            else{
                if(right == s.size() - 1 && !is_equal(record_s, record_t))
                    break;
                if(right - left + 1 < res.size())
                    res = s.substr(left, right - left + 1);
                record_s[s[left++]]--;
            }
        }
        if(res == s + "#")
            return "";
        return res;
    }

    bool is_equal(unordered_map<char, int> l1, unordered_map<char, int> l2){
        for(auto c: l2)
            if(l1.find(c.first) == l1.end() or c.second > l1[c.first])
                return false;
        return true;
    }

    unordered_map<char, int> get_record(string t){
        unordered_map<char, int> res;
        for(auto c: t)
            res[c]++;
        return res;
    }
};