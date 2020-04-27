#include<cstdlib>


class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        srand(NULL);
        return partition(nums, 0, nums.size() - 1, k);
    }

    int partition(vector<int>& nums, int left, int right, int k){
        // 左闭右闭区间，left==right也是有效区间，所以left>right才是无效的区间。
        if(left > right)
            return 0x3fffffff;

        int rand_idx = left + (rand() % (right - left + 1));
        swap(nums[left], nums[rand_idx]);
        int target = nums[left];

        int lt = left;
        int i = left + 1;

        // 普通的单路快排partition思想
        while(i <= right){
            if(nums[i] < target)
                swap(nums[i++], nums[++lt]);
            else
                i++;
        }
        swap(nums[left], nums[lt]);

        if(lt < nums.size() - k)
            return partition(nums, lt + 1, right, k);
        else if(lt > nums.size() - k)
            return partition(nums, left, lt - 1, k);
        return nums[lt];
    }

    void swap(int& num1, int& num2){
        int tmp = num1;
        num1 = num2;
        num2 = tmp;
    }
};