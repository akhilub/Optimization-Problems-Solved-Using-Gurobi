\ Model stadium
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  Z1
Subject To
 R0: S_1 - S_2 <= -2
 R1: S_2 - S_3 <= -16
 R2: S_2 - S_4 <= -16
 R3: S_2 - S_14 <= -16
 R4: S_3 - S_5 <= -9
 R5: S_4 - S_6 <= -8
 R6: S_4 - S_7 <= -8
 R7: S_4 - S_9 <= -8
 R8: S_4 - S_10 <= -8
 R9: S_4 - S_15 <= -8
 R10: S_5 - S_6 <= -10
 R11: S_6 - S_8 <= -6
 R12: S_6 - S_11 <= -6
 R13: S_6 - S_9 <= -6
 R14: S_7 - S_13 <= -2
 R15: S_8 - S_16 <= -2
 R16: S_9 - S_12 <= -9
 R17: S_10 - S_End <= -5
 R18: S_11 - S_16 <= -3
 R19: S_12 - S_17 <= -2
 R20: S_13 - S_End <= -1
 R21: S_14 - S_15 <= -7
 R22: S_15 - S_16 <= -4
 R23: S_16 - S_End <= -3
 R24: S_17 - S_18 <= -9
 R25: S_18 - S_End <= -1
 R26: - Z1 + S_End = 0
Bounds
Generals
 Z1 S_1 S_2 S_3 S_4 S_5 S_6 S_7 S_8 S_9 S_10 S_11 S_12 S_13 S_14 S_15 S_16
 S_17 S_18 S_End
End
