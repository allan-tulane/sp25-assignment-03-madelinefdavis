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

