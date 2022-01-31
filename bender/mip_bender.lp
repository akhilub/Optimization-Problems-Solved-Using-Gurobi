\ Model mip_bender
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  5 x1 - 2 x2 + 9 x3 + n
Subject To
 c1: - 17 x1 - 3 x2 - 5 x3 >= -25
 c2: - 5 x1 + 3 x2 + 7 x3 >= 5
 c3: 5 x1 - 3 x2 - 7 x3 + n <= -5
 c4: 3.833333333333333 x1 - 0.8333333333333334 x2 - 2.166666666666667 x3
   + n <= 0.833333333333333
 c5: 5.333333333333333 x1 + 2.666666666666667 x2 + 5.333333333333333 x3 + n
   <= 13.33333333333333
 c6: 12 x1 + 6 x2 + 12 x3 + n <= 30
Bounds
 x1 <= 5
 x2 <= 5
 x3 <= 5
Generals
 x1 x2 x3
End
