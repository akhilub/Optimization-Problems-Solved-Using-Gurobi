import gurobipy as gp
from gurobipy import GRB

used_tank,used_cap=gp.multidict(
    {2:400,
     7:800
     })

#print(len(used_tank))


Product,NEQty=gp.multidict(
    {'gasoline-grade-80':900,
     'gasoline-grade-90':700,
     'gasoline-grade-93':1000,
     'Diesel'           :450,
     'Engine-Oil'       :700
     })
    

Tank,Cap=gp.multidict(
    {1:500,
     3:400,
     4:600,
     5:600,
     6:900,
     8:800,
     9:800
    })

tank,cap=gp.multidict(
    {2:400,
     7:800
     })

#print(Cap[3])
#p=len(Product)
#t=len(Tank)

m= gp.Model("problem4")
Z=m.addVar(vtype=GRB.INTEGER,obj = 1,name="Z")

x={}
for i in Product:
    for k in Tank:
        x[i,k] = m.addVar(vtype=GRB.BINARY, obj=1, name="x_{}_{}".format(i,k))
        
        
m.update()
m.setObjective(Z,GRB.MINIMIZE)


for k in Tank:
    m.addConstr(gp.quicksum(x[i,k] for i in Product)<=1)
    
for i in Product:
    m.addConstr(gp.quicksum(Cap[k]*x[i,k] for k in Tank)>=NEQty[i])


m.addConstr(gp.quicksum(Cap[k]*x[i,k] for k in Tank for i in Product)==Z)

m.optimize()

if m.status == GRB.status.OPTIMAL:
    m.write("problem4.lp")
    m.write("problem4.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
    
print('Obj: %g' % m.objVal)
print('Total Capacity used =',m.objVal+used_cap[2]+used_cap[7])

Tank_Used=len(used_tank)
for i in Product:
    for k in Tank:
        if (x[i,k].x==1):
            Tank_Used+=x[i,k].x

print('Min no. of tank used =',Tank_Used)

