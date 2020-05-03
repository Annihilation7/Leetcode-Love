

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int good_count = 0;
        int m = grid.size(), n = grid[0].size();
        queue<vector<int>> q;
        int d[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        int res = 0;

        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 1)
                    good_count++;  // 记录好橘子的数量
                if(grid[i][j] == 2)
                    q.push(vector<int>{i, j, 0});  // 将坏橘子的坐标，以及当前时间戳加入队列中
            }

        // bfs
        while(!q.empty()){
            vector<int> front_elem = q.front();
            int i = front_elem[0], j = front_elem[1], time_step = front_elem[2];
            q.pop();
            for(int dis_idx = 0; dis_idx < 4; dis_idx++){
                int new_i = i + d[dis_idx][0];
                int new_j = j + d[dis_idx][1];
                if(check_valid(new_i, new_j, m, n) && grid[new_i][new_j] == 1){
                    good_count--;
                    if(good_count == 0)
                        return time_step + 1;  // 可以提前退出，减少耗时
                    grid[new_i][new_j] = 0;  // 不是1,2就行
                    q.push(vector<int>{new_i, new_j, time_step + 1});
                    res = time_step + 1;
                }
            }
        }
        return good_count == 0 ? res : -1;
    }

    bool check_valid(int i, int j, int m, int n){
        return i >= 0 && i < m && j >= 0 && j < n;
    }
};