#Reference:-Demetrios Papazaharias(TA)

import gurobipy as gp
from gurobipy import GRB

W = [ 0, 0, 0]
weights = [34,6,8,17,16,5,13,21,25,31,14,13,33,9,25,25]

w = len(W)
#print(w)
b = len(weights)
#print(b)

m= gp.Model("problem1")
Z=m.addVar(vtype=GRB.INTEGER, lb = 0, ub = 100, obj = 1,  name="Z")

x={}
for i in range(b):
    for j in range(w):
        x[i+1,j+1] = m.addVar(vtype=GRB.BINARY, obj=1, name="x_{}{}".format(i+1,j+1))

m.update()
m.setObjective(Z,GRB.MINIMIZE)

for i in range(b):
    m.addConstr(gp.quicksum(x[i+1,j+1]  for j in range(w)) == 1)

for j in range(w):
    m.addConstr(gp.quicksum(weights[i]*x[i+1,j+1] for i in range(b)) <= Z)


m.optimize()

print('Obj: %g' % m.objVal)

if m.status == GRB.status.OPTIMAL:
    m.write("problem1.lp")
    m.write("problem1.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
    
        
for j in range(w):
    for i in range(b):
        if (x[i+1,j+1].X)>0.5:
            W[j]+=weights[i]

for j in range(w):
    print("Weight of Wagon{} = ".format(j+1) ,W[j],'kgs')

