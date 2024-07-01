def shortedtCommonSuperSequence(s1,s2,x,y):
    dp=[[0]*(y+1) for _ in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i==0 or j==0:
                dp[i][j]=0
            else:
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        
    return len(s1+s2)-dp[x][y]


X='abcd'
Y='xycd'
print(shortedtCommonSuperSequence(X,Y,len(X),len(Y)))