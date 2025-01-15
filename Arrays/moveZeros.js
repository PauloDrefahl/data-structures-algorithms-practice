/**
 * @param {number[]} nums
 * @return {void} 
 */

var moveZeroes = function(nums) {
    let nonZeroIndex = 0; // Pointer to place the next non-zero element
    
    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            nums[nonZeroIndex] = nums[i];
            nonZeroIndex++;
        }
    }
    
    // Fill the rest of the array with zeros
    for (let i = nonZeroIndex; i < nums.length; i++) {
        nums[i] = 0;
    }

    return nums
};

console.log(moveZeroes([0,1,0,3,12]))