
class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        // 异或运算考察
        int k = 0;
        // 找到那两个只出现一次的值的二者异或
        for(auto c: nums)
            k ^= c;

        // find mask
        int mask = 1;
        while((k & mask) == 0)
            mask <<= 1;

        // 再遍历一次，二者中的一个肯定和mask相与为0，另一个就是其它所有值的异或
        // 用到了 0和任何数的 异或均为本身的特点
        int a = 0;
        int b = 0;
        for(auto c: nums){
            if((c & mask) == 0)
                a ^= c;
            else
                b ^= c;
        }
        return vector<int>{a, b};
    }
};