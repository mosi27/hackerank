Given below is the generic approach / pseudo code for any n * n magic square
Say 's' is the given matrix,
    
    #Get rows and cols len
    rows_len = len(s)
    cols_len = 0 if rows > 0 else len(s[0])
    
    #Get range 
    n = rows * cols
    
    #Get magic sum
    tot_sum = (n * (n + 1) ) / 2  
    magic_sum = tot_sum / rows
    
    #All magic square compute cost
    magic_sqr_cost = []
    
    #Get all permutations for 1 to n
    x = [1,2, ..... n]
    
    #For each permutation, identify magic square and compute the cost 
    for a in permutations(x, n):
      if (sum(row1) ... sum(rows_len) == magic_sum and
           sum(col1) ... sum(cols_len) == magic_sum and
           sum(diagonal_1) == magic_sum and
           sum(diagonal_2) == magic_sum):
            
            #calculate cost
            cost = 0
            a_idx = 0
            for (i in range(rows_len)):
              for (j in range(cols_len)):
                cost += abs(s[i][j] - a[a_idx])
                a_idx++
                
            magic_sqr_cost.append(cost)    
                  
    #Return the min cost
    print(min(magic_sqr_cost)) 
