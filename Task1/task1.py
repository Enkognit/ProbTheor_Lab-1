import math
from scipy import special

n = 20
null_level = [0] * (n + 1)

def stirling(r, j):
    if j > r:
        return 0
    res = 0
    for i in range(j):
        res += math.pow(-1, i) * special.comb(j, i) * math.pow(j - i, r)
    return res

def eval_new_level(ans, dp):
    dp.append([0] * (n + 1))
    for i in range(1, n + 1):
        res = 0
        for j in range(1, n + 1):
            res += dp[-2][j] / math.pow(n + 1, 2 * j) * stirling(2 * j, i)
        dp[-1][i] = res * special.comb(n, i)
    res = 0
    for i in range(1, n + 1):
        res += dp[-1][i]
    ans.append(res)

if __name__ == "__main__":
    level = 10
    ans = [1]
    dp = [[0] * (n + 1)]
    dp[0][1] = 1
    for i in range(level):
        eval_new_level(ans, dp)
        print(i + 1, ": answer -", ans[-1], "; partical answers - ", dp[-1][1:])





