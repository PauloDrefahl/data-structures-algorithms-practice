/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    p1 = 0
    dups = {}
    for(let i = 0; i < nums.length; i++){
        if(!(nums[i] in dups)){
            dups[nums[i]] = 1;
            nums[p1] = nums[i]
            p1++;
        } else {
            dups[nums[i]]++
        }
    }
    return p1;
};

nums = [1,1,2];
removeDuplicates(nums);