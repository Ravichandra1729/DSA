# def maxTurbulenceSize(arr):

    # n=len(arr)
    
    # dp=[0]*n
    # dp[0]=1
    
    # for i in range(n):
        # if i==0:
            # dp[i]=1
        # elif i==1:
            # if arr[i]!=arr[i-1]:
                # dp[i]=2
            # else:
                # dp[i]=1
        # else:
            # if (arr[i]>arr[i-1] and arr[i-1]<arr[i-2]) or (arr[i]<arr[i-1] and arr[i-1]>arr[i-2]):
                # dp[i]=1+dp[i-1]
            # else:
                # if arr[i]!=arr[i-1]:
                    # dp[i]=2
                # else:
                    # dp[i]=1
    # return max(dp)



def maxTurbulenceSize(arr):

    n=len(arr)
    
    dp=0
    ans=0
    
    for i in range(n):
        if i==0:
            dp=1
        elif i==1:
            if arr[i]!=arr[i-1]:
                dp=2
            else:
                dp=1
        else:
            if (arr[i]>arr[i-1] and arr[i-1]<arr[i-2]) or (arr[i]<arr[i-1] and arr[i-1]>arr[i-2]):
                dp=1+dp
            else:
                if arr[i]!=arr[i-1]:
                    dp=2
                else:
                    dp=1
        ans=max(ans,dp)
    return ans





arr=[9,4,2,10,7,8,8,1,9]


print(maxTurbulenceSize(arr))