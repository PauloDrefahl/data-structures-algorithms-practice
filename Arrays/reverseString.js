/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let arr = [...s] 
    let arr2 = [] 

    for(i = arr.length-1; i >= 0; i--) { 
        arr2.push(arr[i]) 
    }
    s = arr2;
    return s
};

console.log(reverseString('test'))