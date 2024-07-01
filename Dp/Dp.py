#Recurssion
def fib(n):
    if n==0:
        return 0;
    elif(n==1):
        return 1;
    else:
        return fib(n-1)+fib(n-2);
print(fib(8))


#dp
def fib1(n,dp):
    if(n==0):
        return 0
    elif(n==1):
        return 1;
    elif(dp[n]!=-1):
        return dp[n]
    else:
        dp[n]=fib1(n-1,dp)+fib1(n-2,dp)
        return dp[n]
n=10
dp=[-1]*(n+1)
print(fib1(n,dp))