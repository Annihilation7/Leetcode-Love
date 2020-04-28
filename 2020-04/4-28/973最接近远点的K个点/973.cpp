#include <queue>

// 学到了，C++自定义排序，需顶定义一个结构体！

class Solution {
public:
    struct cmp {
        bool operator () (vector<int>& a, vector<int>& b) {
            return pow(long(a[0]), 2) + pow(long(a[1]), 2) < pow(long(b[0]), 2) + pow(long(b[1]), 2);
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<vector<int>> res;
        if(points.empty())
            return res;

        priority_queue<vector<int>, vector<vector<int>>, cmp> que;
        for(int i = 0; i < points.size(); i++){
            que.push(points[i]);
            if(que.size() > K)
                que.pop();
        }
        while(!que.empty()){
            res.push_back(que.top());
            que.pop();
        }
        return res;
    }
};