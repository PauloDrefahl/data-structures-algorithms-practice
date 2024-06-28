/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max = nums[0];
    let min = nums[0];

    for(let i = 0; i < nums.length; i++){
        currentNum = currentNum + nums[i];

        if (max < currentNum){
            max = currentNum;
            maxIndex = i;
        }
        if (min > currentNum) {
            currentNum = 0
            min = currentNum;
        }
    }
    
    return max;
};

nums = [-2,1,-3,4,-1,2,1,-5,4]
console.log(maxSubArray(nums))