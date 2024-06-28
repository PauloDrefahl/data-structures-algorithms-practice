/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// var twoSum = function(nums, target) {
//     for(i = 0; i < nums.length; i++){
//         for (j = i+1; j < nums.length; j++){

//             if (nums[i] + nums[j] === target){
//                 console.log(i, j);
//             }
//         }
//     }
// };

nums = [3,2,4];
target = 6;

var twoSum = function(nums, target) {
    const pairIndex = {};
     for(let i = 0; i < nums.length; i++){
         if((target - nums[i]) in pairIndex){
            console.log(pairIndex)
            return [nums[i], target-nums[i]];
         }
         pairIndex[nums[i]] = target - nums[i];
     }
 };

 console.log(twoSum(nums, target))