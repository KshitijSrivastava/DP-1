
## Problem1 (https://leetcode.com/problems/coin-change/)

class Solution:
    #recursuive solution
    def coinChange_recur(self, coins, amount):
        if amount == 0:                                     #if amount == 0, no coin req
            return 0
        elif amount < 0:                                    #if amount < 0, no coin possible
            return float('inf')
        
        num_coins = []
        for coin in coins:                                  #try all possible coin combination
            num = 1 + self.coinChange_recur(coins, amount - coin)
            num_coins.append(num)
        return min( num_coins )                             #find the minimum of the number of coins
    
    
    #memoization
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        
        def coinChange_recur(coins, amount):
            if amount == 0:                             #if the amount is zero, no coin in required 
                return 0
            elif amount < 0:                            #if amount < 0, no coin combination possible
                return float('inf')
            elif amount in dp:                          #if amount calc already in dp, return it
                return dp[amount]
            
            num_coins = []
            for coin in coins:                          #try all possible conbinations with coins
                num = 1 + coinChange_recur(coins, amount - coin)
                num_coins.append(num)
            
            dp[amount] = min( num_coins )               #find the minimum combination
            return dp[amount]
            
            
        ret_value = coinChange_recur(coins, amount)
        #print(ret_value)

        if ret_value == float('inf'):
            return -1
        return ret_value

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = []                                         #initlizae the dp table
        for i in range( len(coins) + 1 ):
            dp.append( [0 for j  in range(amount + 1)] )
            
        for j in range(amount + 1):                     #first row is made of infinity
            dp[0][j] = float('inf')
            
        for i in range( len(coins) + 1 ):               #first column is made of 0
            dp[i][0] = 0
        
        for i in range(1, len(coins) + 1):
            for j in range( 1, amount + 1 ):
                if coins[i-1] <= j:                     #if amount is greater or equal to coin amount
                    dp[i][j] =  min( dp[i-1][j], 1 + dp[i][j - coins[i-1] ] ) 
                else:                                   # if amount is less then the coin amount 
                    dp[i][j] = dp[i-1][j]
                    
        if dp[len(coins)][amount] == float('inf'):
            return -1
        return dp[len(coins)][amount]