\ Model MIP
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  5 x_1 - 2 x_2 + 9 x_3 + 2 y_1 - 3 y_2 + 4 y_3
Subject To
 R0: 5 x_1 - 3 x_2 - 7 x_3 + 2 y_1 + 3 y_2 + 6 y_3 <= 2
 R1: 4 x_1 + 2 x_2 + 4 x_3 + 3 y_1 - y_2 + 3 y_3 <= 10
Bounds
 x_1 <= 5
 x_2 <= 5
 x_3 <= 5
Generals
 x_1 x_2 x_3
End
