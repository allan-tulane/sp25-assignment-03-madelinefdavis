# CMPS 2200 Assignment 3
## Answers

**Name:** Madeline Davis

Place all written answers from `assignment-03.md` here for easier grading.

**1a)**

find the highest power of 2 that is less than or equal to N

subtract this value from N

repeat this process with the next highest power of 2 that is less than or equal to N

continue unti $N=0$

code: 

  def min_coins(N):
  
    coins = []
    
    while N > 0:
    
        highest_power = 1
        
        while highest_power * 2 <= N:
        
            highest_power *= 2
            
        coins.append(highest_power)
        
        N -= highest_power
        
    return coins

**1b)**

this algorthim always selects the largest possible coin at each step. since it is powers of 2 no smaller combination will sum to N with fewer coins

**1c)**

the work and span are both $O(log n)$


**2a)** consider the demoninations = {10, 7, 1} and N=14

if we were to use a greedy algrothim the first pick would be 10 followed by one being picked 4 times. This results in 5 coins being used. Instead an optimal solution would be to pick 7 twice. This means we would use 2 coins instead of 7.

**2b** 

a problem follow the optimal substructure property if an optimal solution can be constructed from breaking it into subproblems.

**2c**

  def min_coins(N, denominations):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for coin in denominations:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[N] if dp[N] != float('inf') else -1
