class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // 找一个起始歧义点就完事了
        if(matrix.size() == 0)
            return false;

        int start_x = matrix.size() - 1;
        int start_y = 0;

        while(start_x >= 0 && start_y < matrix[0].size()){
            if(matrix[start_x][start_y] < target)
                start_y++;
            else if(target < matrix[start_x][start_y])
                start_x--;
            else
                return true;
        }
        return false;
    }
};