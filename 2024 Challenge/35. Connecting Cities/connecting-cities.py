mode = 1 # 0 = test, 1 = input

options = [40, 12, 2, 1] if mode else [3, 2, 1]
distance = 856 if mode else 5

dp = [0] * (distance + 1)
dp[0] = 1
for i in range(1, distance + 1):
    for option in options:
        if i >= option:
            dp[i] += dp[i - option]
print(dp[distance])
