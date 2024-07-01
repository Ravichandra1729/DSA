# def issubsetsum(N,arr,sum1):
    # dp={}
    # arr.sort(reverse=True)
    # def solve(n,sm):
        # if n==0:
            # return 0
        # elif sm==0:
            # return 1
        # elif(n,sm) in dp:
            # return dp[(n,sm)]
        # else:
            # item=arr[n-1]
            # if item<=sm:
                # c1=solve(n-1,sm)
                # c2=solve(n-1,sm-item)
                # c=c2 or c1
            # else:
                # c=0
                # #c=solve(n-1,sm)
            # dp[(n,sm)]=c
        # return c
    # return solve(N,sum1)
# print(issubsetsum(6,[3,34,4,12,5,2],9))

#tabulation
def issubsetsum(N,arr,sum1):
    dp=[[0]*(sum1+1)for _ in range(N)]
    for i in range(N):
        for j in range(sum1+1):
            item=arr[i]
            sm=j 
            if i==0:
                if sm==0 or item==sm:
                    dp[i][j]=1
            else:
                if item<sm:
                    dp[i][j]=dp[i-1][sm-item] or dp[i-1][sm]
                else:
                    dp[i][j]=dp[i-1][sm]
    return dp[N-1][sum1]
print(issubsetsum(6,[3,34,4,12,5,2],9))