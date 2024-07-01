#kadane's algotitham

# def maxSubArray(arr):
    # n=len(arr)
    # dp=[0]*n
    # dp[0]=arr[0]
    # for i in range(1,n):
        # c1=arr[i]
        # c2=dp[i-1]+arr[i]
        # dp[i]=max(c1,c2) 
    # return max(dp)
    
    
    
def maxSubArray(arr):
    n=len(arr)
    temp=arr[0]
    mx=arr[0]
    for i in range(1,n):
        c1=arr[i]
        c2=temp+arr[i]
        temp=max(c1,c2) 
        mx=max(mx,temp)
    return mx
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))