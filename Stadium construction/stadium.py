import gurobipy as gp
from gurobipy import GRB

Task,t,Maxr,Cost = gp.multidict(
    {
        1: [2,0,0],
        2: [16,3,30],
        3: [9,1,26],
        4: [8,2,12],
        5: [10,2,17],
        6: [6,1,15],
        7: [2,1,8],
        8: [2,0,0], 
        9: [9,2,42],
        10: [5,1,21 ],
        11: [3,1,18],
        12: [2,0,0],
        13: [1,0,0],
        14: [7,2,22],
        15: [4,2,12],
        16: [3,1,6],
        17: [9,3,16],
        18: [1,0,0 ],
        'End':[0,0,0], 
    }
)


Arcs =((1,2),(2,3),(2,4),(2,14),(3,5),(4,6),(4,7),(4,9),(4,10),(4,15),(5,6),(6,8),(6,11),(6,9),
       (7,13),(8,16),(9,12),(10,'End'),(11,16),(12,17),(13,'End'),(14,15),(15,16),(16,'End'),(17,18),(18,'End'))


m =gp.Model('stadium')

Z1= m.addVar(vtype=GRB.INTEGER,obj=1, name="Z1")
   
S={}
for i in Task:
    S[i] = m.addVar(vtype=GRB.INTEGER,obj=1,lb=0,name="S_{}".format(i))

#m.modelSense = GRB.MAXIMIZE
m.setObjective(Z1,GRB.MINIMIZE)

m.update()

for i,j in Arcs:
    m.addConstr(S[i]+t[i]<=S[j])


m.addConstr(S['End']==Z1)


m.optimize()


print('least possible number of weeks required for completing the construction of the stadium: %g' % m.objVal)

if m.status == GRB.status.OPTIMAL:
    m.write("stadium.lp")
    m.write("stadium.sol")
    
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')