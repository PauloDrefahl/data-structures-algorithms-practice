//this would work for a non sorted array
var removeDuplicates = function(nums) {
    p1 = 0
    dups = {}
    for(let i = 0; i < nums.length; i++){
        if(!(nums[i] in dups)){
            dups[nums[i]] = 1;
            nums[p1] = nums[i]
            p1++;
        } else if (dups[nums[i]] < 2) {
            dups[nums[i]]++
            nums[p1] = nums[i]
            p1++;
        } else {
            dups[nums[i]]++
        }
    }
    return p1;
    
};

nums = [1,1,1,2,2,3];
removeDuplicates(nums);

//you can probably solve this using two pointers, more efficient but prob would only work for sorted arrays
// start with two pointers, one faster and one slower, change the faster in case condition is satisfied, do not change otherwise
// in this case the "deepth" is k = 2 because it is sorted and the condition is two duplicates.

var removeDuplicatesTwoPointer = function(nums) {
    if(nums.length <= 2) {
        return nums.length;
    }

    let k = 2;

    for(let i = 2; i < nums.length; i++){

        if(nums[i] != nums[k - 2] || nums[i] != nums[k - 1]){
            nums[k] = nums[i];
            k++;
        }
        
        console.log(nums)
    }
    return k;      
};

nums = [1,1,1,2,2,3];
removeDuplicatesTwoPointer(nums);