#longestIncreasingSubsequence

# def longestIncreasingSubsequence(a,n):
    # dp={}
    # def solve(arr,n,li):
        # if n==0:
            # return 0
        # elif (n,li) in dp:
            # return dp[(n,li)]
        # else:
            # if li==-1 or arr[n-1]<arr[li]:
                # c1=1+solve(arr,n-1,n-1)
                # c2=solve(arr,n-1,li)
                # c=max(c1,c2)
            # else:
                # c=solve(arr,n-1,li)

        # dp[(n,li)]=c
        # return c
    # return solve(a,n,-1)
    
    
    
def longestIncreasingSubsequence(a,n):
    dp=[0]*n
    dp[0]=1
    for i in range(1,n):
        ce=a[i]
        j=i-1
        max1=0
        while j>=0:
            if a[j]<ce:
                max1=max(max1,dp[j])
            j-=1
        dp[i]=1+max1

    return max(dp)
N=16
A=[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
print(longestIncreasingSubsequence(A,N))