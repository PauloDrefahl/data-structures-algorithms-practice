function reverseNums(nums, start, end) {
    while(start < end){
        let temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
 }

function rotate(nums, k) {
   k = k % nums.length;
   reverseNums(nums, 0, nums.length-1);
   reverseNums(nums, 0, k-1);
   reverseNums(nums, k, nums.length - 1);
}





// Example usage
let nums1 = [1, 2, 3, 4, 5, 6, 7];
rotate(nums1, 3);
console.log(nums1); // Output: [5, 6, 7, 1, 2, 3, 4]

let nums2 = [-1, -100, 3, 99];
rotate(nums2, 2);
console.log(nums2); // Output: [3, 99, -1, -100]
