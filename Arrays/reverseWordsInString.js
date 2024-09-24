/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    arr = s.split(' ')
    arr = arr.filter(element => element !== '')

    let left = 0;
    let right = arr.length - 1;


    // this is again a really important algortithm to be reused in case of reversing an array
    while (left < right) {
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }

    return (arr.join(' '))
};


reverseWords("  hello world  ")