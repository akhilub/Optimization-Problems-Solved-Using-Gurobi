Solves the problem:


min c1*x + c2*y

st  A1*x + A2*y <=b (m constraints)

x binary n1-dimensional vector
    
y >=0 continuous n2-dimensional vector
    
    
c1 = [1,6,5,7]                    # n1 x 1

c2 = [9,3,0,2,3]                  # n2 x 1

b  = [-3,-4,1,4,5]                # m  x 1


         [  0 -2  3  2]        [ 1 2 3 ]            [ a*1 b*2 c*3 ]
    A1 = [ -5  0 -3  1]    B = [ 4 5 6 ]    A * B = [ d*4 e*5 f*6 ]
         [  1  0  4 -2]        [ 7 8 9 ]            [ g*7 h*8 i*9 ]
         [  0 -3  4 -1]
         [ -5 -4  3  0]

A1 = [0 -2 3  2]                          
     [-5, 0,-3, 1]
     [1 , 0, 4,-2]
     [0 ,-3, 4,-1]
     [-5,-4, 3, 0]

A2 = [[3, 4, 2, 0, -5],
      [0, 2, 3, -2, 1],
      [2, 0, 1, -3, -5],
      [-5, 3, -2, -3, 0],
      [-2, 3, -1, 2, -4]]
