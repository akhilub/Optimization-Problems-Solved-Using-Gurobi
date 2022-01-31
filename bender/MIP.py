#### Solves the problem:
#### min c*x + h*y
#### st  A*x + G*y <=b (m constraints)
#### x integer n1-dimensional vector
#### y >=0 continuous n2-dimensional vector

import gurobipy as gp
from gurobipy import GRB

c = [5,-2,9]

h = [2, -3, 4]

A=[[5,-3,-7],
    [4,2,4]]

G=[[2,3,6],
[3,-1,3]]

b=[2,10]



m=gp.Model("MIP")

#### Define Variables
x={}
for i in range(len(c)):
    x[i+1] = m.addVar(vtype=GRB.INTEGER,lb=0,ub=5,obj=1, name="x_{}".format(i+1))

y={}
for j in range(len(h)):
    y[j+1] = m.addVar(vtype=GRB.CONTINUOUS,lb=0,obj=1, name="y_{}".format(j+1))


#### Define Objective
m.setObjective(gp.quicksum(c[i]*x[i+1] for i in range(len(c))) +\
               gp.quicksum(h[j]*y[j+1] for j in range(len(h))),\
               sense=GRB.MAXIMIZE)

#### Define Constraints

for k in range(len(b)):
    m.addConstr(gp.quicksum(A[k][i]*x[i+1] for i in range(len(c))) +\
          gp.quicksum(G[k][j]*y[j+1] for j in range(len(h)))\
                        <=b[k])


m.update()

m.optimize()
print('Obj:{}'.format(m.objVal))

for v in m.getVars():
    print('{}={}'.format(v.varName,v.x))



if m.status == GRB.status.OPTIMAL:
    m.write("MIP.lp")
    m.write("MIP.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # It tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')