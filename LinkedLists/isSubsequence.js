function isSubsequence(s, t) {
    let sp = 0, tp = 0;
    while (tp < t.length) {
        if (s[sp] === t[tp]) {
            sp++;
        }
        tp++;
    }
    return sp === s.length;
}