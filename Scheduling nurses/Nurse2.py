import gurobipy as gp
from gurobipy import GRB

T=[i for i in range(1,13)] 
#print(T)
N=len(T)
#print(N)
R=[15,15,15,35,40,40,40,30,31,35,30,20]

W=[0,-1,-3,-4]

MAX=80

m =gp.Model('nurse')

Z= m.addVar(vtype=GRB.INTEGER,obj=1, name="Z")

S={}
for t in T:
    S[t-1] = m.addVar(vtype=GRB.INTEGER,obj=1,lb=0,name="S_{}".format(t))
            
ET={}
for t in T:
    ET[t-1] = m.addVar(vtype=GRB.INTEGER,obj=1,lb=0,name="ET_{}".format(t))
    
m.setObjective(Z,GRB.MINIMIZE)

m.update()

m.addConstr(gp.quicksum(ET[t-1] for t in T)==Z)

m.addConstr(gp.quicksum(S[t-1] for t in T)<=MAX)

for t in T:
    m.addConstr(ET[t-1]<=S[t-1])

for t in T:
    m.addConstr((ET[(t-1-5+N) % N] + gp.quicksum(S[(t-1+i+N) % N] for i in W)) >= R[t-1])
    
m.optimize()

print('Obj: %g' % m.objVal)

if m.status == GRB.status.OPTIMAL:
    m.write("nurse2.lp")
    m.write("nurse2.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')

