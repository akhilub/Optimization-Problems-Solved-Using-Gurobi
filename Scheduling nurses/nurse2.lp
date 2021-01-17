\ Model nurse
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  Z
Subject To
 R0: - Z + ET_1 + ET_2 + ET_3 + ET_4 + ET_5 + ET_6 + ET_7 + ET_8 + ET_9
   + ET_10 + ET_11 + ET_12 = 0
 R1: S_1 + S_2 + S_3 + S_4 + S_5 + S_6 + S_7 + S_8 + S_9 + S_10 + S_11
   + S_12 <= 80
 R2: - S_1 + ET_1 <= 0
 R3: - S_2 + ET_2 <= 0
 R4: - S_3 + ET_3 <= 0
 R5: - S_4 + ET_4 <= 0
 R6: - S_5 + ET_5 <= 0
 R7: - S_6 + ET_6 <= 0
 R8: - S_7 + ET_7 <= 0
 R9: - S_8 + ET_8 <= 0
 R10: - S_9 + ET_9 <= 0
 R11: - S_10 + ET_10 <= 0
 R12: - S_11 + ET_11 <= 0
 R13: - S_12 + ET_12 <= 0
 R14: S_1 + S_9 + S_10 + S_12 + ET_8 >= 15
 R15: S_1 + S_2 + S_10 + S_11 + ET_9 >= 15
 R16: S_2 + S_3 + S_11 + S_12 + ET_10 >= 15
 R17: S_1 + S_3 + S_4 + S_12 + ET_11 >= 35
 R18: S_1 + S_2 + S_4 + S_5 + ET_12 >= 40
 R19: S_2 + S_3 + S_5 + S_6 + ET_1 >= 40
 R20: S_3 + S_4 + S_6 + S_7 + ET_2 >= 40
 R21: S_4 + S_5 + S_7 + S_8 + ET_3 >= 30
 R22: S_5 + S_6 + S_8 + S_9 + ET_4 >= 31
 R23: S_6 + S_7 + S_9 + S_10 + ET_5 >= 35
 R24: S_7 + S_8 + S_10 + S_11 + ET_6 >= 30
 R25: S_8 + S_9 + S_11 + S_12 + ET_7 >= 20
Bounds
Generals
 Z S_1 S_2 S_3 S_4 S_5 S_6 S_7 S_8 S_9 S_10 S_11 S_12 ET_1 ET_2 ET_3 ET_4
 ET_5 ET_6 ET_7 ET_8 ET_9 ET_10 ET_11 ET_12
End
