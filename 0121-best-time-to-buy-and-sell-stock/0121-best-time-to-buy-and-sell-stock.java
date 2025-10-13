class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int minBuy = prices[0];

        for (int price : prices) {
            if (price < minBuy) minBuy = price;                 // best (cheapest) buy so far
            else maxProfit = Math.max(maxProfit, price - minBuy); // best profit if sold today
        }
        return maxProfit;
    }
}
