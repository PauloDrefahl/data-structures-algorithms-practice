//questions 1: 
/* basically you just need to start 3 pointers, one for the last index of each list and one for the end index of nums1 + nums2
we start by comparing the last item of each and then inserting to the very end the largest item. decreasing them as we add to the end. 
*/

var merge = function(nums1, m, nums2, n) {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    
    while (j >= 0) {
        if (i >= 0 && nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
};

let nums1 = [1,2,3,0,0,0];
let nums2 = [2,5,6];

merge(nums1, 3, nums2, 3);

//less effective solution o(n)

mergeSortedArrays([0,3,4,31], [3,4,6,30]);

function mergeSortedArrays(arr1, arr2){
    var mergedArray = []
        for(let i = 0; i < arr1.length; i++){
            for(let j = 0; j < arr2.length; j++){
                if (arr1[i] <= arr2[j]){
                    mergedArray.push(arr1[i])
                } 
                else {
                    mergedArray.push(arr2[j])
                }
            }
        }
    return mergedArray
}

console.log(mergeSortedArrays([0,3,4,31], [3,4,6,30])); 