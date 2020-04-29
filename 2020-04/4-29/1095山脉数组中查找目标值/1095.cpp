/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        // 先找山顶，然后分段二分即可
        // 注意找山顶的二分算法，很有考究的。
        int res = -1;
        int moutain_top = find_mountaintop(mountainArr);
        res = find_num_ascend(target, mountainArr, 0, moutain_top);
        if(res != -1)
            return res;
        res = find_num_descend(target, mountainArr, moutain_top + 1, mountainArr.length() - 1);
        if(res != -1)
            return res;
        return -1;
    }

    int find_mountaintop(MountainArray& mountainArr){
        int left = 0;
        int right = mountainArr.length() - 1;

        while(left < right){
            int mid = left + (right - left) / 2;
            if(mountainArr.get(mid) < mountainArr.get(mid + 1))
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    int find_num_ascend(int target, MountainArray& mountainArr, int left, int right){
        while(left < right){
            int mid = left + (right - left) / 2;
            if(target > mountainArr.get(mid))
                left = mid + 1;
            else
                right = mid;
        }
        return mountainArr.get(left) == target ? left : -1;
    }

    int find_num_descend(int target, MountainArray& mountainArr, int left, int right){
        while(left < right){
            int mid = left + (right - left) / 2;
            if(target < mountainArr.get(mid))
                left = mid + 1;
            else
                right = mid;
        }
        return mountainArr.get(left) == target ? left : -1;
    }
};