#### Solves the problem:
#### min c1*x + c2*y
#### st  A1*x + A2*y <=b (m constraints)
#### x binary n1-dimensional vector
#### y >=0 continuous n2-dimensional vector

################################################################################
#########################  PROBLEM INITIALIZATIONS   ###########################
################################################################################

#### Import Necessary Packages
import gurobipy as gp
from gurobipy import GRB
#import sys

#### Initialize Problem Parameters
c1 = [1,6,5,7]                    # n1 x 1

c2 = [9,3,0,2,3]                  # n2 x 1

b  = [-3,-4,1,4,5]                # m  x 1

A1 = [[0, -2, 3, 2],
      [-5, 0, -3, 1],
      [1, 0, 4, -2],
      [0, -3, 4, -1],
      [-5, -4, 3, 0]]

A2 = [[3, 4, 2, 0, -5],
      [0, 2, 3, -2, 1],
      [2, 0, 1, -3, -5],
      [-5, 3, -2, -3, 0],
      [-2, 3, -1, 2, -4]]

m  = len(b)
n1 = len(c1)
n2 = len(c2)

#### Absolute accuracy for optimal objective
ObjAbsAccuracy=0.00001
################################################################################
#####################       SOLVE ORIGINAL PROBLEM        ######################
################################################################################
#### Solves the problem without decomposing.

#### Define Problem
p = gp.Model()

#### Define Variables
x={}
for i in range(n1):
    x[i] = p.addVar(vtype=GRB.BINARY,obj=1, name="x_{}".format(i))

#x = [p.addVar(vtype=GRB.BINARY) for i in range(n1)]
y={}
for j in range(n2):
    y[j] = p.addVar(vtype=GRB.CONTINUOUS,obj=1, name="y_{}".format(j))


#y = [p.addVar(vtype=GRB.CONTINUOUS) for i in range(n2)] #positive real variable


#### Define Constraints

for k in range(m):
    p.addConstr(gp.quicksum(A1[k][i]*x[i] for i in range(n1)) +\
          gp.quicksum(A2[k][j]*y[j] for j in range(n2))\
                        <=b[k])




#### Define Objective
p.setObjective(gp.quicksum(c1[i]*x[i] for i in range(n1)) +\
               gp.quicksum(c2[j]*y[j] for j in range(n2)),\
               sense=GRB.MINIMIZE)

p.update()
#### Solve and retrieve solution
p.optimize()

if p.status == GRB.status.OPTIMAL:
    p.write("MIP.lp")
    p.write("MIP.sol")
elif p.status == GRB.status.INFEASIBLE:
    p.computeIIS() # IIS tells you which constraints, when removed, makes the m feasible
    p.write('inf.ilp')

#To print all decision variables together
for v in p.getVars():
    print('{}={}'.format(v.varName,v.x))


#To print decision variables individually

print("The first stage variables are:")
for i in range(n1):
    print('{}={}'.format(x[i].varName,x[i].x))

print("The second stage variables are:")
for j in range(n2):
    print(y[j].varName,'=',y[j].x)

#To print objective function values individually

print("The optimal objective is:", p.objVal)


print("The objective of the second stage is:\n",\
       sum(c2[j]*y[j] for j in range(n2)),'=',sum(c2[j]*y[j].x for j in range(n2)))
