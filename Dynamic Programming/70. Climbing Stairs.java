class Solution {
    public int climbStairs(int n) {
        // Base cases: 1 way to climb 0 or 1 step.
        if (n == 0 || n == 1) {
            return 1;
        }
        
        // dp array to store the number of ways to climb to each step
        int[] dp = new int[n + 1];
        // Base cases initialization
        dp[0] = 1;
        dp[1] = 1;
        
        // Bottom-up calculation from step 2 to n
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        // The final element of the array is the answer.
        return dp[n];
    }
}