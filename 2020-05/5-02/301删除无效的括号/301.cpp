//
// Created by nofalling on 2020/5/1.
//


class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        // bfs的问题，而且会有重复的括号产生，所以要用set
        unordered_set<string> record = {s};
        while(record.size() > 0){
            vector<string> cur_res = set2vector(record, is_valid);
            if(cur_res.size() > 0)
                return cur_res;
            unordered_set<string> new_res;
            for(auto c: record)
                if(c.size())
                    for(int i = 0; i < c.size(); i++)
                        if(c[i] == '(' || c[i] == ')'){
                            string copy_c = c;  // 注意erase是in-place的删除操作！！
                            new_res.insert(copy_c.erase(i, 1));
                        }
            record = new_res;
        }
        return vector<string>();
    }

    static bool is_valid(const string& s){
        // 通过计数变量来判断是否是正确的括号组合，不用开辟模拟空间了
        int cnt = 0;
        for(auto c: s){
            if(cnt < 0)
                return false;
            if(c == '(')
                cnt++;
            else if(c == ')')
                cnt--;
        }
        return cnt == 0;
    }

    vector<string> set2vector(const unordered_set<string>& record, bool (*filter)(const string&)){
        vector<string> res;
        for(auto c: record)
            if(filter(c))
                res.push_back(c);
        return res;
    }
};