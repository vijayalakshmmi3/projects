def knapsack(val,weight,n,cap):
    if n==0 or cap==0:
        return 0
    if weight[n-1]>cap:
        knapsack(val,weight,n-1,cap)
    else:
        return max(val[n-1]+knapsack(val,weight,n-1,cap-weight[n-1]),
    knapsack(val,weight,n-1,cap))
capacity=50
val=[100,250,300]
w=[10,20,30]
n=len(w)
print(knapsack(val,w,n,capacity))
