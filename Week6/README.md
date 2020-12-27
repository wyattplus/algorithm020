学习笔记
# week-6 
DP课程题目相对较难，需要多花时间去消化理解。
# 动态规划关键点
## 1. 最优子结构 opt[n] = best_of(opt[n-1], opt[n-2], …)
## 2. 储存中间状态：opt[i]
## 3. 递推公式（状态转移方程或者 DP 方程） 
例如：Fib: opt[i] = opt[n-1] + opt[n-2] 
二维路径：opt[i,j] = opt[i+1][j] + opt[i][j+1] (且判断a[i,j]是否空地）

![week6](/Xmind/week6.png)