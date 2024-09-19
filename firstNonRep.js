/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    s = s.split('')
    characters = {}
    for(let i = 0; i < s.length; i++){
        if (!(s[i] in characters)){
            characters[s[i]] = 1;
        } else {
            characters[s[i]]++;
        }
    }

    for(let [key, value] of Object.entries(characters)){
        if (value < 2){
            return s.indexOf(key)
        }
    }
}
s = "loveleetcode"
console.log(firstUniqChar(s))