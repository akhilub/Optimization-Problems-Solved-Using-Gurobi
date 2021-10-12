# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 23:02:40 2021

@author: akhil
"""
import gurobipy as gp
from gurobipy import GRB

VC_D2C=[[100,80,50,50,60,100,120,90,60,70,65,110],
     [120,90,60,70,65,110,140,110,80,80,75,130],
     [140,110,80,80,75,130,160,125,100,100,80,150],
     [160,125,100,100,80,150,190,150,130,1000,1000,1000],
     [190,150,130,1000,1000,1000,200,180,150,1000,1000,1000],
     [200,180,150,1000,1000,1000,100,80,50,50,60,100],
     [100,80,50,50,60,100,120,90,60,70,65,100],
     [120,90,60,70,65,110,140,110,80,80,72,130],
     [140,110,80,80,75,130,160,125,100,100,80,150],
     [160,125,100,100,80,150,190,150,130,1000,1000,1000],
     [190,150,130,1000,1000,1000,200,180,150,1000,1000,1000],
     [200,180,150,1000,1000,1000,100,80,50,50,60,100]]

Dem=[120,80,75,100,110,100,90,60,30,150,95,120]
Cap=[300,250,100,180,275,300,200,220,270,250,230,180]

FC=[3500,9000,10000,4000,3000,9000,9000,3000,4000,10000,9000,3500]
#print(D2C)
D=len(VC_D2C)
print(D)
C=len(VC_D2C[0])
#for c in range(C):
    #print(len(VCD2C[c]))

#print(Dem)
#print(Cap)


m=gp.Model("problem3")

TC=m.addVar(vtype=GRB.CONTINUOUS, lb = 0, obj = 1, name="TC")

x={}
for j in range(D):
    x[j+1] = m.addVar(vtype=GRB.BINARY,obj=1, name="x_{}".format(j+1))
    
y={}
for j in range(D):
    for i in range(C):
        y[j+1,i+1]=m.addVar(vtype=GRB.CONTINUOUS,lb=0,ub=1,obj=1,name="y_{},{}".format(j+1,i+1))

m.update()
#m.modelSense = GRB.MINIMIZE
m.setObjective(TC,GRB.MINIMIZE)

for i in range(C):
    m.addConstr(gp.quicksum(y[j+1,i+1] for j in range(D)) ==1)


for j in range(D):
    m.addConstr(gp.quicksum(Dem[i]*y[j+1,i+1] for i in range(C))<=(Cap[j]*x[j+1]))

m.addConstr((gp.quicksum(FC[j]*x[j+1] for j in range(D))+(gp.quicksum(VC_D2C[j][i]*y[j+1,i+1] for i in range(C) for j in range(D))))==TC)
    
m.optimize()

if m.status == GRB.status.OPTIMAL:
    m.write("problem3.lp")
    m.write("problem3.sol")
elif m.status == GRB.status.INFEASIBLE:
    m.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    m.write('inf.ilp')
    
print('Total Minimum Cost= $%g' % m.objVal)

