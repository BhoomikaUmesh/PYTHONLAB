def knapsack_max_profit(weights,costs,capacity):
  num_items=len(weights)
  table=[[0]*(capacity+1) for _ in range(num_items+1)]
  for i in range(1,num_items+1):
    for j in range(1,capacity+1):
      if weights[i-1]<=j:
        table[i][j] = max(costs[i-1]+table[i-1][j-weights[i-1]],table[i-1][j])
      else:
        table[i][j]=table[i-1][j]  