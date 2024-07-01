import sys
sys.setrecursionlimit(5000)
# def knapsack(N,W,val,wt):
    # dp={}
    # def solve(n,cap):
        # if n==0 or cap==0:
            # return 0
        # elif(n,cap) in dp:
            # return dp[(n,cap)]
        # else:
            # cw=wt[n-1]
            # cv=val[n-1]
            # if cw<=cap:
                # c1=cv+solve(n,cap-cw)
                # c2=solve(n-1,cap)
                # c=max(c1,c2)
                
            # else:
                # c=solve(n-1,cap)
            # dp[(n,cap)]=c
            # return c
        
    # return solve(N,W)
    
# def knapsack(N,W,val,wt):
    # dp=[[0]*(W+1) for _ in range(N)]
    # for i in range(N):
        # for j in range(W+1):
            # cap=j 
            # cv=val[i]
            # cw=wt[i]
            # if i==0:
                # dp[i][j]=(cap//cw)*cv
                    
            # else:
                # if cw<=cap:
                    # dp[i][j]=max(cv+dp[i][cap-cw],dp[i-1][cap])
                # else:
                    # dp[i][j]=dp[i-1][cap]
    # return dp[N-1][W]           


def knapsack(N,W,val,wt):
    dp=[0]*(W+1)
    for i in range(N):
        for j in range(W+1):
            cap=j 
            cv=val[i]
            cw=wt[i]
            if i==0:
                dp[j]=(cap//cw)*cv
                    
            else:
                if cw<=cap:
                    dp[j]=max(cv+dp[cap-cw],dp[cap])
                else:
                    dp[j]=dp[cap]
    return dp[W]                      
    




    
N=2
W=3
val=[1,1]
wt=[2,1]
print(knapsack(N,W,val,wt))