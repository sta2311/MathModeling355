# 例1.1     7.14   
# https://pypi.tuna.tsinghua.edu.cn/simple
from pulp import *

prob = LpProblem("problem1",LpMaximize)

x1 = LpVariable("x1",0,None,LpContinuous)
x2 = LpVariable("x2",0,None,LpContinuous)

prob += 4000*x1+3000*x2

prob += 2* x1 + 1 * x2 <= 10
prob += x1 + x2 <= 8
prob += x2 <= 7

prob.writeLP("problem.lp")

prob.solve()

print("\n","status:",LpStatus[prob.status],"\n")

for v in prob.variables():
    print("\t",v.name,"=",v.varValue,"\n")

print("Maximun Daily Profit =","Rs",value(prob.objective))