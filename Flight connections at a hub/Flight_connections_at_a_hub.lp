\ Model Flight_connections_at_a_hub
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  Z
Subject To
 R0: - Z + 35 cont_1_1 + 12 cont_1_2 + 16 cont_1_3 + 38 cont_1_4
   + 5 cont_1_5 + 2 cont_1_6 + 25 cont_2_1 + 8 cont_2_2 + 9 cont_2_3
   + 24 cont_2_4 + 6 cont_2_5 + 8 cont_2_6 + 12 cont_3_1 + 8 cont_3_2
   + 11 cont_3_3 + 27 cont_3_4 + 3 cont_3_5 + 2 cont_3_6 + 38 cont_4_1
   + 15 cont_4_2 + 14 cont_4_3 + 30 cont_4_4 + 2 cont_4_5 + 9 cont_4_6
   - 1000 cont_5_1 + 9 cont_5_2 + 8 cont_5_3 + 25 cont_5_4 + 10 cont_5_5
   + 5 cont_5_6 - 1000 cont_6_1 - 1000 cont_6_2 - 1000 cont_6_3
   + 14 cont_6_4 + 6 cont_6_5 + 7 cont_6_6 = 0
 R1: cont_1_1 + cont_2_1 + cont_3_1 + cont_4_1 + cont_5_1 + cont_6_1 = 1
 R2: cont_1_2 + cont_2_2 + cont_3_2 + cont_4_2 + cont_5_2 + cont_6_2 = 1
 R3: cont_1_3 + cont_2_3 + cont_3_3 + cont_4_3 + cont_5_3 + cont_6_3 = 1
 R4: cont_1_4 + cont_2_4 + cont_3_4 + cont_4_4 + cont_5_4 + cont_6_4 = 1
 R5: cont_1_5 + cont_2_5 + cont_3_5 + cont_4_5 + cont_5_5 + cont_6_5 = 1
 R6: cont_1_6 + cont_2_6 + cont_3_6 + cont_4_6 + cont_5_6 + cont_6_6 = 1
 R7: cont_1_1 + cont_1_2 + cont_1_3 + cont_1_4 + cont_1_5 + cont_1_6 = 1
 R8: cont_2_1 + cont_2_2 + cont_2_3 + cont_2_4 + cont_2_5 + cont_2_6 = 1
 R9: cont_3_1 + cont_3_2 + cont_3_3 + cont_3_4 + cont_3_5 + cont_3_6 = 1
 R10: cont_4_1 + cont_4_2 + cont_4_3 + cont_4_4 + cont_4_5 + cont_4_6 = 1
 R11: cont_5_1 + cont_5_2 + cont_5_3 + cont_5_4 + cont_5_5 + cont_5_6 = 1
 R12: cont_6_1 + cont_6_2 + cont_6_3 + cont_6_4 + cont_6_5 + cont_6_6 = 1
Bounds
Binaries
 cont_1_1 cont_1_2 cont_1_3 cont_1_4 cont_1_5 cont_1_6 cont_2_1 cont_2_2
 cont_2_3 cont_2_4 cont_2_5 cont_2_6 cont_3_1 cont_3_2 cont_3_3 cont_3_4
 cont_3_5 cont_3_6 cont_4_1 cont_4_2 cont_4_3 cont_4_4 cont_4_5 cont_4_6
 cont_5_1 cont_5_2 cont_5_3 cont_5_4 cont_5_5 cont_5_6 cont_6_1 cont_6_2
 cont_6_3 cont_6_4 cont_6_5 cont_6_6
Generals
 Z
End
