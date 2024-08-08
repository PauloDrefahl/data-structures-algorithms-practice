/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    
    for (let i = 0; i < prices.length; i++) { 
        if (prices[i] < minPrice) { //see if the price is the minimum and stablish minimum
            minPrice = prices[i];
        } else if (prices[i] - minPrice > maxProfit) { // if it is not the minimum price, and the current - minimum is larger than the max profit. we have a new max profit  
            maxProfit = prices[i] - minPrice;
        }
    }
    
    return maxProfit;
};

prices = [7,6,4,3,1]; //example

maxProfit(prices);