import math
N = int(input())
M = int(input())

dp = [100001 for i in range(M+1)]
dp[N] = 0
for i in range(N, M-1):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            k = i + j
            if k <= M:
                dp[k] = min(dp[k],dp[i] + 1)

            k = i + int(i/j)
            if k <= M:
                dp[k] = min(dp[k],dp[i] + 1)
if dp[M] == 100001:
    print(-1)
else:
    print(dp[M])

