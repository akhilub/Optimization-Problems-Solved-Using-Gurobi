\ Model nurse
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  Z
Subject To
 R0: - Z + S_1 + S_2 + S_3 + S_4 + S_5 + S_6 + S_7 + S_8 + S_9 + S_10
   + S_11 + S_12 = 0
 R1: S_1 + S_9 + S_10 + S_12 >= 15
 R2: S_1 + S_2 + S_10 + S_11 >= 15
 R3: S_2 + S_3 + S_11 + S_12 >= 15
 R4: S_1 + S_3 + S_4 + S_12 >= 35
 R5: S_1 + S_2 + S_4 + S_5 >= 40
 R6: S_2 + S_3 + S_5 + S_6 >= 40
 R7: S_3 + S_4 + S_6 + S_7 >= 40
 R8: S_4 + S_5 + S_7 + S_8 >= 30
 R9: S_5 + S_6 + S_8 + S_9 >= 31
 R10: S_6 + S_7 + S_9 + S_10 >= 35
 R11: S_7 + S_8 + S_10 + S_11 >= 30
 R12: S_8 + S_9 + S_11 + S_12 >= 20
Bounds
Generals
 Z S_1 S_2 S_3 S_4 S_5 S_6 S_7 S_8 S_9 S_10 S_11 S_12
End
