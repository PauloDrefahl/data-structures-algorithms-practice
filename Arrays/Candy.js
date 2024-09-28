function candy(ratings) {
    const n = ratings.length, candies = Array(n).fill(1);
    for (let i = 1; i < n; i++) if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
    for (let i = n - 2; i >= 0; i--) if (ratings[i] > ratings[i + 1]) candies[i] = Math.max(candies[i], candies[i + 1] + 1);
    return candies.reduce((a, b) => a + b, 0);
}
const ratings = [1, 0, 2];
console.log(candy(ratings));