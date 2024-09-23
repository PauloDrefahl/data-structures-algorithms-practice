function isSubsequence(s, t) {
    let s = 0, t = 0;
    while (t < t.length) {
        if (s[s] === t[t]) {
            s++;
        }
        t++;
    }
    return s === s.length;
}