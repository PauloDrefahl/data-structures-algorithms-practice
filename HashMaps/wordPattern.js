var wordPattern = function(pattern, s) {
    let s_arr = s.split(" ");
    let p_arr = pattern.split("");
    
    if (s_arr.length !== p_arr.length) {
        return false; 
    }

    let pattern_to_word = new Map();
    let word_to_pattern = new Map();

    for (let i = 0; i < p_arr.length; i++) {
        let char = p_arr[i];
        let word = s_arr[i];

        if (pattern_to_word.has(char)) {
            if (pattern_to_word.get(char) !== word) {
                return false;
            }
        } else {
            pattern_to_word.set(char, word);
        }

        if (word_to_pattern.has(word)) {
            if (word_to_pattern.get(word) !== char) {
                return false; 
            }
        } else {
            word_to_pattern.set(word, char);
        }
    }

    return true;
};




console.log(wordPattern("abba", "dog dog dog dog"))

