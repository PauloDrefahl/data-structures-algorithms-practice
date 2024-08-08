/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let maxReach = 0;
    
    for (let i = 0; i < nums.length; i++) {
        if (i > maxReach) {
            return false;
        }

        maxReach = Math.max(maxReach, i + nums[i]);
        
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }
    
    return false;
};

let nums = [3, 2, 1, 0, 4];
console.log(canJump(nums)); // Should print false
