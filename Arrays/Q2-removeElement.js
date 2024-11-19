
/*
Questiosn 2: Basically Just have two variables, one that is gping to iterate through the list and another that will only be added in case the values do not match.
Then, if the values do not match with the value to remove, you just need to add to that slower moving pointer variable to the one iterating through every thing.
remember that you need to return the new size for the list wich would be the slower moving variable.

class Solution(object):
    def removeElement(self, nums, val):
        p1 = 0
        i = 0
        while (i < len(nums)):
            if(nums[i] != val):
                nums[p1] = nums[i]
                p1 += 1
            i += 1

        return p1
*/




function removeElement(nums, val) {
    let k = 0;
    for( let i = 0; i < nums.length; i++){
        if(nums[i] !== val){
            nums[k++] = nums[i]; 
        }
    }
    return nums;
}

nums = [3,2,2,3];
val = 3;

console.log(removeElement(nums, val))