import gurobipy as gp
from gurobipy import GRB

T=[i for i in range(1,13)] 
#print(T)
N=len(T)
#print(N)
R=[15,15,15,35,40,40,40,30,31,35,30,20]

W=[0,-1,-3,-4]


m =gp.Model('nurse')

Z= m.addVar(vtype=GRB.INTEGER,obj=1, name="Z")

S={}
for t in T:
    S[t-1] = m.addVar(vtype=GRB.INTEGER,obj=1,lb=0,name="S_{}".format(t))
    
m.setObjective(Z,GRB.MINIMIZE)

m.update()


m.addConstr(gp.quicksum(S[t-1] for t in T)==Z)

for t in T:
    m.addConstr(gp.quicksum(S[(t-1+i+N) % N] for i in W) >= R[t-1])
    
m.optimize()

print('Obj: %g' % m.objVal)

if m.status == GRB.status.OPTIMAL:
    m.write("nurse.lp")
    m.write("nurse.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')