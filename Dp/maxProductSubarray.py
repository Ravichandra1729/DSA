# def maxProduct(arr):
    # n=len(arr)
    # mx=[0]*(n)
    # mn=[0]*(n)
    # mx[0]=arr[0]
    # mn[0]=arr[0]
    # for i in range(1,n):
        
        # el=arr[i]
        # c1=el 
        # c2=el*mn[i-1]
        # c3=el*mx[i-1]
        # mx[i]=max(c1,c2,c3)
        # mn[i]=min(c1,c2,c3)
    # return max(mx)
    
    
    
def maxProduct(arr):
    n=len(arr)
    mx=arr[0]
    mn=arr[0]
    ans=arr[0]
    for i in range(1,n):
        
        el=arr[i]
        c1=el 
        c2=el*mn
        c3=el*mx
        mx=max(c1,c2,c3)
        mn=min(c1,c2,c3)
        ans=max(ans,mx)
    return ans
arr=[2,3,-2,4]
print(maxProduct(arr))