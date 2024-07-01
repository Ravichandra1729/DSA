# def knapsack(W,wt,val,N):
    # def solve(n,cap):
        # if n==0 or cap==0:
            # return 0;
        # else:
            # cwt=wt[n-1]
            # cv=val[n-1]
            # if cwt<=cap:
                # c1=cv+solve(n-1,cap-cwt)
                # c2=solve(n-1,cap)
                # return max(c1,c2)
            # else:
                # return solve(n-1,cap)
    # return solve(N,W)
# N=3
# W=4
# values=[1,2,3]
# weight=[4,5,1]
# print(knapsack(W,weight,values,N))

#now using dp :

# def knapsack(W,wt,val,N):
    # def solve(n,cap):
        # dp={}
        # if n==0 or cap==0:
            # return 0;
        # elif(n,cap) in dp:
            # return dp[(n,cap)]
        # else:
            # cwt=wt[n-1]
            # cv=val[n-1]
            # if cwt<=cap:
                # c1=cv+solve(n-1,cap-cwt)
                # c2=solve(n-1,cap)
                # c= max(c1,c2)
            # else:
                # c=solve(n-1,cap)
            # dp[(n,cap)]=c 
            # return c
    # return solve(N,W)
# N=3
# W=4
# values=[1,2,3]
# weight=[4,5,1]
# print(knapsack(W,weight,values,N))


#iterative approch:
def knapsack(W,wt,val,N):
    dp=[[0]*(W+1)for i in range(N) ]
    for i in range(N):
        for j in range(W+1):
            cap=j
            cwt=wt[i]
            cv=val[i]
            if i==0:
                if cwt<=cap:
                    dp[i][j]=cv
                else:
                    dp[i][j]=0
            else:
                if cwt<=cap:
                    c1=cv+dp[i-1][cap-cwt]
                    c2=dp[i-1][cap]
                    dp[i][j]=max(c1,c2)
                else:
                    dp[i][j]=dp[i-1][cap]
                        
        
    return dp[N-1][W]
N=3
W=4
values=[1,2,3]
weight=[4,5,1]
print(knapsack(W,weight,values,N))



