#### Solves the problem:
#### min c*x + h*y
#### st  A*x + G*y <=b (m constraints)
#### x integer n1-dimensional vector
#### y >=0 continuous n2-dimensional vector

### using bender decomposition

import gurobipy as gp
from gurobipy import GRB

m=gp.Model("mip_bender")
x1=m.addVar(vtype=GRB.INTEGER,lb=0,ub=5,name="x1")
x2=m.addVar(vtype=GRB.INTEGER,lb=0,ub=5,name="x2")
x3=m.addVar(vtype=GRB.INTEGER,lb=0,ub=5,name="x3")

n=m.addVar(vtype=GRB.CONTINUOUS,lb=0,name="n")

m.setObjective(5*x1-2*x2+9*x3+n,GRB.MAXIMIZE)

#Feasibility Cuts
m.addConstr((-2-(5*x1-3*x2+3-7*x3))*1+(10-(4*x1+2*x2+4*x3))*3 >=0,"c1")
m.addConstr((-2-(5*x1-3*x2+3-7*x3))*1+(10-(4*x1+2*x2+4*x3))*0 >=0,"c2")

#Optimality Cuts
m.addConstr(n <= -2-(5*x1-3*x2+3-7*x3),"c3")

m.addConstr(n <= (1/2)*(-2-(5*x1-3*x2+3-7*x3))+(1/3)*(10-(4*x1+2*x2+4*x3)),"c4")

m.addConstr(n <= (4/3)*(10-(4*x1+2*x2+4*x3)),"c5")

m.addConstr(n <= (3)*(10-(4*x1+2*x2+4*x3)),"c6")

m.update()

m.optimize()
print('Obj:{}'.format(m.objVal))

for v in m.getVars():
    print('{}={}'.format(v.varName,v.x))


if m.status == GRB.status.OPTIMAL:
    m.write("mip_bender.lp")
    m.write("mip_bender.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # It tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')