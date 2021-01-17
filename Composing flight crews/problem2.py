import gurobipy as gp
from gurobipy import GRB

Pilot,Eng,Fre,Dut,Nor,Reco,Tran,Bomb,Figh,Supp = gp.multidict(
    {
        1: [20,12, 0,0 ,18,0 ,0 ,0 ,0 ],
        2: [14,0 ,20,0 ,12,17,17,0 ,0 ],
        3: [0 ,0 ,12,0 ,15,0 ,0 ,14,0 ],
        4: [13,10,0 ,0 ,0 ,11,11,0 ,0 ],
        5: [0 ,15,8 ,17,0 ,13,13,0 ,12],
        6: [0 ,20,11,0 ,0 ,10,10,12,18],
        7: [8 ,8 ,14,0 ,8 ,0 ,0 ,16,0 ],
        8: [8 ,9 ,12,16,0 ,0 ,0 ,0 ,18], 
    }
)

Arcs,scores = gp.multidict({
(1,2): 30,
(2,3): 27,
(2,4): 28,
(2,6): 27,
(3,6): 26,
(3,7): 30,
(4,5): 24,
(4,6): 21,
(5,6): 30,
(5,8): 30,
(6,7): 28,
(6,8): 36,
})

Arcs = gp.tuplelist(Arcs)
#print(Pilot)
#print(Arcs)
#print(scores[(1, 2)])

m =gp.Model('problem2')

Z= m.addVar(vtype=GRB.INTEGER,obj=1, name="Z")
   
x={}
for i, j in Arcs:
    x[i,j] = m.addVar(vtype=GRB.BINARY,obj=1, name="x_{}{}".format(i,j))

#m.modelSense = GRB.MAXIMIZE
m.setObjective(Z,GRB.MAXIMIZE)

m.update()

for p in Pilot:
    m.addConstr(gp.quicksum(x[i,j] for i,j in Arcs.select(p,'*')) + gp.quicksum(x[j,i] for j,i in Arcs.select('*',p)) <= 1)
    

m.addConstr((gp.quicksum(x[i,j] for i,j in Arcs))==Z)
#m.addConstr((gp.quicksum(scores[i,j]*x[i,j] for i,j in Arcs))==Z)


m.optimize()

print('Obj: %g' % m.objVal)

if m.status == GRB.status.OPTIMAL:
    m.write("problem2.lp")
    m.write("problem2.sol")
    
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
    
#Part (b) of problem2
crew_score=0
for i, j in Arcs:
    if x[i, j].x>0.5:
        crew_score+=scores[i,j]*x[i,j].x
        print('Arc (%s,%s): %g' % (i, j, scores[i, j]))
        #print(crew_score)
        
#This also do the same work as above        
#crew_score=0
#if(x[i,j].x==1):
    #crew_score=sum(scores[i,j]*x[i,j].x for i, j in Arcs)
     #print('Arc (%s,%s): %g' % (i, j, scores[i, j]))   

print("Crew Score",crew_score)





