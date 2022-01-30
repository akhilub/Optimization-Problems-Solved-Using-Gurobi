import gurobipy as gp
from gurobipy import GRB
import math

PLANES=[1,2,3,4,5,6]

PASS=[[35,12,16,38,5,2],
[25,8,9,24,6,8],
[12,8,11,27,3,2],
[38,15,14,30,2,9],
[-1000,9,8,25,10,5],
[-1000,-1000,-1000,14,6,7]
]

m=gp.Model("Flight_connections_at_a_hub")

m.update()

#n= len(PLANES)

Z=m.addVar(vtype=GRB.INTEGER, obj = 1, name="Z")

cont={}
for i in PLANES:
    for j in PLANES:
        cont[i,j] = m.addVar(vtype=GRB.BINARY, obj=1, name="cont_{}_{}".format(i,j))


m.addConstr(gp.quicksum(PASS[i-1][j-1]*cont[i,j] for j in PLANES for i in PLANES)==Z)

m.setObjective(Z,GRB.MAXIMIZE)

for j in PLANES:
    m.addConstr(gp.quicksum(cont[i,j] for i in PLANES)==1)

for i in PLANES:
    m.addConstr(gp.quicksum(cont[i,j] for j in PLANES)==1)


m.optimize()

print('Obj:{}'.format(m.objVal))

if m.status == GRB.status.OPTIMAL:
    m.write("Flight_connections_at_a_hub.lp")
    m.write("Flight_connections_at_a_hub.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
