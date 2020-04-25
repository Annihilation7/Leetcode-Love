class Solution {
public:
    void mergeSort(vector<int>& nums) {
    	if(nums.size() == 0)
    		return nums;

    	_mergeSort(nums, 0, nums.size() - 1);
    }

    void _mergeSort(vector<int>& nums, int l, int r){
    	if(l >= r)
    		return;

    	mid = l + (r - l) / 2;
    	_mergeSort(nums, l, mid);
    	_mergeSort(nums, mid + 1, r);
    	_merge(nums, l, mid, r);
    }

    void _merge(vector<int>& nums, int l, int mid, int r){
    	int* aux = new int[r - l + 1];
    	for(int i = l; i <= r; i++)
    		aux[i - l] = nums[i];

    	int i = l;
    	int j = mid + 1;
    	for(int k = l; k <= r; k++){
    		if(i > mid)
    			nums[k] = aux[j++ - l];
    		else if(j > r)
    			nums[k] = aux[i++ - l];
    		else if(aux[i - l] <= aux[j - l])
    			nums[k] = aux[i++ - l];
    		else
    			nums[k] = aux[j++ - l];
    	}
    }
};
