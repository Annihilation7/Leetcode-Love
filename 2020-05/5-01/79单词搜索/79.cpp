

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        vector<vector<bool>> visited = vector<vector<bool>>(m, vector<bool>(n, false));  // 是可以省掉的，这里就不省了哈
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(helper(board, visited, word, 0, i, j))
                    return true;  // 找到就提前终止，一个剪枝操作
        return false;
    }

    bool helper(
        const vector<vector<char>>& board, 
        vector<vector<bool>>& visited,  // 前面两个参数完美诠释 形参 和 实参 的区别！用形参绝壁超时！！！找了半天问题！
        const string& word, 
        int cur_idx, 
        int x, int y
    ){
        if(cur_idx == word.size())  // 这个条件必须放前面，放后面的话就要cur_idx == word.size() - 1; retun board[x][y] == word[cur_idx]
        // 好好想想为什么，提示要注意下面的条件哦
            return true;
        if(!is_valid(x, y, board.size(), board[0].size()) || visited[x][y] || board[x][y] != word[cur_idx])
            return false;

        visited[x][y] = true;
        bool res = helper(board, visited, word, cur_idx + 1, x - 1, y) || \
                   helper(board, visited, word, cur_idx + 1, x, y + 1) || \
                   helper(board, visited, word, cur_idx + 1, x + 1, y) || \
                   helper(board, visited, word, cur_idx + 1, x, y - 1);
        visited[x][y] = false;  // traceback

        return res;
    }

    bool is_valid(int x, int y, int m, int n){
        return x >= 0 and y >= 0 and x < m and y < n;
    }
};