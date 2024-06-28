/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let arr = [...s] // transform string in an array
    let arr2 = [] // create an empty string

    for(i = arr.length-1; i >= 0; i--) { //loop from last index of the first array to the first
        arr2.push(arr[i]) //add to the new array
    }
    s = arr2;
    return s
};

console.log(reverseString('test'))