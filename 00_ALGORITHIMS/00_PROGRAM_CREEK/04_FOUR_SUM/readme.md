### Four sum

* Given an array of $S$ integers, are there elements $a$, $b$, $c$ and $d$ in $S$ such that $a+b+c+d=t$, where $t$ is the target.
* Find all unique quadruplets in the array which gives the sum of the target.

* **Note:** elements in a quadruplet $(a,b,c,d)$ must be in a non-descending order.
* The solution set must not contain duplicate quadruplets.

Example:

````python
S = [1, 0, -1, 0, -2, 2]
t = 0
Answer: [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
````

Code:

````python
def four_sum(numbers: list, target: int) -> list:
    
    result = []
    
    #don't want to handle empty lists and those with less than 4 numbers
    if not numbers and len(numbers) < 4:
        return result
    
    #use the pointer method when sorting
    numbers = sorted(numbers)
    
    #i is the "start" pointer
    for i in range(len(numbers)-3):
        
        #always do the first number
        #if not doing the first number, skip duplicates
        if i != 0 and numbers[i] == numbers[i-1]:
            continue
            
        #j is a "second start" pointer
        for j in range(i+1, len(numbers)-2):
            
            #always do the second number
            #if not doing the second, skip duplicates
            if j != i+1 and numbers[j] == numbers[j-1]:
                continue
                
            #k and j are the "search start" and "search end" pointers
            k = j + 1
            l = len(numbers)-1
            
            while k < l: #the standard search method here
                                
                x = numbers[i] + numbers[j] + numbers[k] + numbers[l]
                
                #if lower than the target, increase the "search start" pointer
                if x < target:
                    k += 1
                
                #if higher than the target, decrease the "search end" pointer
                elif x > target:
                    l -= 1
                    
                else:
                    
                    #if we find a result, append it
                    result.append([numbers[i],numbers[j],numbers[k],numbers[l]])
                    
                    #move the pointers
                    k += 1
                    l -= 1
                    
                    #while still valid pointers, make sure we ignore duplicates
                    while k < l and numbers[l] == numbers[l+1]:
                        l -= 1
                        
                    while k < l and numbers[k] == numbers[k-1]:
                        k += 1
        
    return result


S = [1, 0, -1, 0, -2, 2]

print(four_sum(S, 0))
````
