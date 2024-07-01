# def lcs(x,y,s1,s2):
    # dp={}
    # s3=list(s1)
    # s4=list(s2)
    # def solve(m,n):
        # if m==0 or n==0:
            # return 0
        # elif (m,n) in dp:
            # return dp[(m,n)]
        # else:
            # if s3[m-1]==s4[n-1]:
                # c= 1+solve(m-1,n-1)
            # else:
                # c1=solve(m,n-1)
                # c2=solve(m-1,n)
                # c=max(c1,c2)
        # dp[(m,n)]=c 
        # return c 
    # return solve(x,y)
    
def lcs(x,y,s1,s2):
    dp=[[0]*(y+1) for _ in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            m=i 
            n=j 
            if m==0 or n==0:
                dp[i][j]=0
            else:
                if s1[m-1]==s2[n-1]:
                    dp[i][j]=1+dp[m-1][n-1]
                else:
                    c1=dp[m-1][n]
                    c2=dp[m][n-1]
                    dp[i][j]=max(c1,c2)
    return dp[x][y]
        

A=6
B=6
str1='ABCDGH'
str2='AEDFHR'
print(lcs(A,B,str1,str2))




# class Solution:
    
    # #Function to find the length of longest common subsequence in two strings.
    # def lcs(self,x,y,str1,str2):
        
        # dp=[[0]*(y+1) for _ in range(x+1)]
        # for i in range(x+1):
            # for j in range(y+1):
                # if i==0 or j==0:
                    # dp[i][j]=0
                # else:
                    # if s1[i-1]==s2[j-1]:
                        # dp[i][j]=1+dp[i-1][j-1]
                    # else:
                        # dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        # return dp[x][y]
        
        
        
        
def longestCommonSubsequence(a,b):
    n=len(a)
    m=len(b)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]==0
            else:
                if a[i-1]==b[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    ans=[]
    i,j=n,m 
    while i>0 and j>0:
        if a[i-1]==b[j-1]:
            ans.append(a[i-1])
            i-=1
            j-=1 
        else:
            if dp[i-1][j]>=dp[i][j-1]:
                i-=1
            else:
                j-=1 
    return ans[::-1]
print(longestCommonSubsequence([1,2,3,4,1],[3,4,1,2,1,3]))
            
            
        
        
        
        