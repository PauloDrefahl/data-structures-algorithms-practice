function calculate(s) {
    let stack = [];
    let result = 0;
    let number = 0;
    let sign = 1;

    for (let i = 0; i < s.length; i++) {
        let char = s[i];

        if (!isNaN(char) && char !== ' ') {
            number = number * 10 + parseInt(char);
        } else if (char === '+') {
            result += sign * number;
            number = 0;
            sign = 1;
        } else if (char === '-') {
            result += sign * number;
            number = 0;
            sign = -1;
        } else if (char === '(') {
            stack.push(result);
            stack.push(sign);
            result = 0;
            sign = 1;
        } else if (char === ')') {
            result += sign * number;
            number = 0;
            result *= stack.pop();
            result += stack.pop();
        }
    }

    if (number !== 0) {
        result += sign * number;
    }

    return result;
}
