

class Solution {
public:
    // 双向BFS，很巧呀
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> record(wordList.begin(), wordList.end());
        if(!record.count(endWord))
            return 0;

        unordered_set<string> fowward = {beginWord};
        unordered_set<string> backward = {endWord};
        int length = beginWord.size();  // 因为都是一样长的，直接记录一下
        int step = 0;  // level

        while(fowward.size() && backward.size()){
            step++;

            // 一种小的优化策略，每次都选小的set开始expand，并且把小的设为forward
            if(fowward.size() > backward.size())
                swap(fowward, backward);

            unordered_set<string> q;
            for (auto c: fowward){
                for(int i = 0; i < length; i++){
                    char tmp = c[i];  // 记录一下，因为后面要变回来，类似回溯
                    for(char character='a'; character <= 'z'; character++){  // 遍历所有可能，相当于在建图
                        c[i] = character;
                        if(backward.count(c))  
                            return step + 1;
                        if(!record.count(c))
                            continue;  // 字典中不存在，continue
                        q.insert(c);
                        record.erase(c);
                    }
                    c[i] = tmp;
                }
            }
            swap(q, fowward);
        }
        return 0;
    }
};