var productExceptSelf = function(nums) {
    let length = nums.length;
    let answer = new Array(length).fill(1);
    
    let leftProduct = 1;
    for (let i = 0; i < length; i++) {
        answer[i] = leftProduct;
        leftProduct *= nums[i];
    }
    
    let rightProduct = 1;
    for (let i = length - 1; i >= 0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }
    
    return answer;
};
