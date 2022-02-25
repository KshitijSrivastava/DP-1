
## Problem2 (https://leetcode.com/problems/house-robber/)

class Solution:
    #Time complexity: 
    #Space Complexity:O(N) stack frames 
    def rob_recur(self, nums, n, idx):
        if idx >= n:                                #if idx greater than house avail, return 0
            return 0
        
        #if the house is robbed, go to house idx +2
        taken = nums[idx] + self.rob_recur(nums, n, idx + 2)
        #if the house is not robbed, go to the next house
        not_taken = self.rob_recur(nums, n, idx + 1)
        
        #find the maximum of the both option
        return max(taken, not_taken)
    
    #memoization
    #Time Complexity: O(N)
    #Space Complexity: O(N)
    def rob(self, nums: List[int]) -> int:
        dp = {}
        
        def rob_recur(nums, n, idx):
            if idx >= n:                            #if idx greater than house avail, return 0
                return 0
            elif idx in dp:                         #if idx is found in dp, return the value
                return dp[idx]
                

            taken = nums[idx] + rob_recur(nums, n, idx + 2)
            not_taken = rob_recur(nums, n, idx + 1)

            dp[idx] = max(taken, not_taken)         #store the answer in the dp
            return dp[idx]
    
        return rob_recur(nums, len(nums), 0)
    
    #Space COmplexity: O(N)
    #Time COmplexity: O(N)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n) ]
        
        dp[0] = nums[0]                             #when only 1st house is robbed, return nums[0]
        
        if n == 1:                                  #if there is only 1 element
            return dp[0]
        
        dp[1] = max(nums[0], nums[1])               #return whatever is the maximum of first 2 houses
        if n == 2:
            return dp[1]
        
        for i in range(2, n):                        
            #either don't rob and take value of prev house or rob and take value of loot in house idx-2   
            dp[i] = max( dp[i-1], dp[i-2] + nums[i] ) 
        
        return dp[n-1]