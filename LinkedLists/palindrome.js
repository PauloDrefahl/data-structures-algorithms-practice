function isPalindrome(s) {
    let cleanedString = s.toLowerCase().replace(/[^a-z0-9]/g, '');
    let reversedString = cleanedString.split('').reverse().join('');
    return cleanedString === reversedString;
}
