/*
Question 3: Basically just create a seen set or liest or hashmap. Create an indexing pointer and a size variable.
If the element has been seen, remove it, if not, then just continue and add it to the seen set, incresing the size variable.
return the size var. 


class Solution(object):
    def removeDuplicates(self, nums):
        seen = set()  
        i = 0 
        size = 0
        
        while i < len(nums):
            if nums[i] in seen: 
                nums.pop(i)
            else:
                seen.add(nums[i])
                i += 1 
                size += 1
        
        return size

*/

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
    console.log(nums, dups, p1);
};

nums = [1,1,2];
removeDuplicates(nums);