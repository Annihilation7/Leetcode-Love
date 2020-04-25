class Solution {

private:
	const vector<string> d1 = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
    		"Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    const vector<string> d2 = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

public:
    string numberToWords(int num) {
    	if(num < 20)
    		return d1[num];
    	
    	string res = "";
    	
    	vector<int> array(4, 0);
    	int i = 3;
    	while(i >= 0){
    		array[i] = num % 1000;
    		num /= 1000;
    		i--;
    	}

    	int j = 0;
    	while(j <= 3){
    		string tmp = "";
    		if(array[j] != 0)
    			tmp = helper(array[j]);
    		else{
    			j++;
    			continue;
    		}
    		if(j == 0)
    			res += tmp + " Billion";
    		else if(j == 1){
    			if(res.size() > 0)
    				res += " ";
    			res += tmp + " Million";
    		}
    		else if(j == 2){
    			if(res.size() > 0)
    				res += " ";
    			res += tmp + " Thousand";
    		}
    		else{
    			if(res.size() > 0)
    				res += " ";
    			res += tmp;
    		}
    		j++;
    	}
    	return res;
    }

    string helper(int num){  // 用于计算1000以内的数
    	string ans = "";
    	if(num >= 100){
    		ans += d1[num / 100] + " Hundred";
    		num %= 100;
    	}
    	if(num >= 20){
    		if(ans.size() > 0)
    			ans += " ";
    		ans += d2[num / 10];
    		num %= 10;
    	}
    	if(num != 0){
    		if(ans.size() > 0)
    			ans += " ";
    		ans += d1[num];   	
    	}
    	return ans;
    }
};