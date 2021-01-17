\ Model problem2
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  Z
Subject To
 R0: x_12 <= 1
 R1: x_12 + x_23 + x_24 + x_26 <= 1
 R2: x_23 + x_36 + x_37 <= 1
 R3: x_24 + x_45 + x_46 <= 1
 R4: x_45 + x_56 + x_58 <= 1
 R5: x_26 + x_36 + x_46 + x_56 + x_67 + x_68 <= 1
 R6: x_37 + x_67 <= 1
 R7: x_58 + x_68 <= 1
 R8: - Z + x_12 + x_23 + x_24 + x_26 + x_36 + x_37 + x_45 + x_46 + x_56
   + x_58 + x_67 + x_68 = 0
Bounds
Binaries
 x_12 x_23 x_24 x_26 x_36 x_37 x_45 x_46 x_56 x_58 x_67 x_68
Generals
 Z
End
