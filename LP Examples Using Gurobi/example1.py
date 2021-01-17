from gurobipy import *

m=Model("mip1")
x=m.addVar(vtype=GRB.CONTINUOUS, name="x")
y=m.addVar(vtype=GRB.CONTINUOUS, name="y")
z=m.addVar(vtype=GRB.CONTINUOUS, name="z")

m.update()

m.setObjective(x+y+2*z,GRB.MAXIMIZE)
m.addConstr(x+2*y+3*z<=4,"c0")
m.addConstr(x+y>=1,"c1")
m.addConstr(x>=0,"c2")
m.addConstr(y>=0,"c3")
m.addConstr(z>=0,"c4")

m.optimize()
print('Obj:{}'.format(m.objVal))

for v in m.getVars():
    print('{}={}'.format(v.varName,v.x))



if m.status == GRB.status.OPTIMAL:
    m.write("example1.lp")
    m.write("example1.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # It tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
    
