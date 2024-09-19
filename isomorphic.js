// in this question focus on identifying if there are conflicts between the strings so you are able to see that they can be swapped

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    map_s = {}
    map_t = {}

    for(let i = 0; i < s.length; i++){
        char_s = s[i]
        char_t = t[i]

        if(map_s[char_s] !== undefined && map_s[char_s] !== char_t){
            return false
        }
        if(map_t[char_t] !== undefined && map_t[char_t] !== char_s){
            return false
        }

        map_s[char_s] = char_t;
        map_t[char_t] = char_s;
    }

    return true;

};

s='paper';
t='title';

console.log(isIsomorphic(s,t))