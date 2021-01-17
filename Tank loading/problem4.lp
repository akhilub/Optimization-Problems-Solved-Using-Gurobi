\ Model problem4
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  Z
Subject To
 R0: x_gasoline-grade-80_1 + x_gasoline-grade-90_1 + x_gasoline-grade-93_1
   + x_Diesel_1 + x_Engine-Oil_1 <= 1
 R1: x_gasoline-grade-80_3 + x_gasoline-grade-90_3 + x_gasoline-grade-93_3
   + x_Diesel_3 + x_Engine-Oil_3 <= 1
 R2: x_gasoline-grade-80_4 + x_gasoline-grade-90_4 + x_gasoline-grade-93_4
   + x_Diesel_4 + x_Engine-Oil_4 <= 1
 R3: x_gasoline-grade-80_5 + x_gasoline-grade-90_5 + x_gasoline-grade-93_5
   + x_Diesel_5 + x_Engine-Oil_5 <= 1
 R4: x_gasoline-grade-80_6 + x_gasoline-grade-90_6 + x_gasoline-grade-93_6
   + x_Diesel_6 + x_Engine-Oil_6 <= 1
 R5: x_gasoline-grade-80_8 + x_gasoline-grade-90_8 + x_gasoline-grade-93_8
   + x_Diesel_8 + x_Engine-Oil_8 <= 1
 R6: x_gasoline-grade-80_9 + x_gasoline-grade-90_9 + x_gasoline-grade-93_9
   + x_Diesel_9 + x_Engine-Oil_9 <= 1
 R7: 500 x_gasoline-grade-80_1 + 400 x_gasoline-grade-80_3
   + 600 x_gasoline-grade-80_4 + 600 x_gasoline-grade-80_5
   + 900 x_gasoline-grade-80_6 + 800 x_gasoline-grade-80_8
   + 800 x_gasoline-grade-80_9 >= 900
 R8: 500 x_gasoline-grade-90_1 + 400 x_gasoline-grade-90_3
   + 600 x_gasoline-grade-90_4 + 600 x_gasoline-grade-90_5
   + 900 x_gasoline-grade-90_6 + 800 x_gasoline-grade-90_8
   + 800 x_gasoline-grade-90_9 >= 700
 R9: 500 x_gasoline-grade-93_1 + 400 x_gasoline-grade-93_3
   + 600 x_gasoline-grade-93_4 + 600 x_gasoline-grade-93_5
   + 900 x_gasoline-grade-93_6 + 800 x_gasoline-grade-93_8
   + 800 x_gasoline-grade-93_9 >= 1000
 R10: 500 x_Diesel_1 + 400 x_Diesel_3 + 600 x_Diesel_4 + 600 x_Diesel_5
   + 900 x_Diesel_6 + 800 x_Diesel_8 + 800 x_Diesel_9 >= 450
 R11: 500 x_Engine-Oil_1 + 400 x_Engine-Oil_3 + 600 x_Engine-Oil_4
   + 600 x_Engine-Oil_5 + 900 x_Engine-Oil_6 + 800 x_Engine-Oil_8
   + 800 x_Engine-Oil_9 >= 700
 R12: - Z + 500 x_gasoline-grade-80_1 + 400 x_gasoline-grade-80_3
   + 600 x_gasoline-grade-80_4 + 600 x_gasoline-grade-80_5
   + 900 x_gasoline-grade-80_6 + 800 x_gasoline-grade-80_8
   + 800 x_gasoline-grade-80_9 + 500 x_gasoline-grade-90_1
   + 400 x_gasoline-grade-90_3 + 600 x_gasoline-grade-90_4
   + 600 x_gasoline-grade-90_5 + 900 x_gasoline-grade-90_6
   + 800 x_gasoline-grade-90_8 + 800 x_gasoline-grade-90_9
   + 500 x_gasoline-grade-93_1 + 400 x_gasoline-grade-93_3
   + 600 x_gasoline-grade-93_4 + 600 x_gasoline-grade-93_5
   + 900 x_gasoline-grade-93_6 + 800 x_gasoline-grade-93_8
   + 800 x_gasoline-grade-93_9 + 500 x_Diesel_1 + 400 x_Diesel_3
   + 600 x_Diesel_4 + 600 x_Diesel_5 + 900 x_Diesel_6 + 800 x_Diesel_8
   + 800 x_Diesel_9 + 500 x_Engine-Oil_1 + 400 x_Engine-Oil_3
   + 600 x_Engine-Oil_4 + 600 x_Engine-Oil_5 + 900 x_Engine-Oil_6
   + 800 x_Engine-Oil_8 + 800 x_Engine-Oil_9 = 0
Bounds
Binaries
 x_gasoline-grade-80_1 x_gasoline-grade-80_3 x_gasoline-grade-80_4
 x_gasoline-grade-80_5 x_gasoline-grade-80_6 x_gasoline-grade-80_8
 x_gasoline-grade-80_9 x_gasoline-grade-90_1 x_gasoline-grade-90_3
 x_gasoline-grade-90_4 x_gasoline-grade-90_5 x_gasoline-grade-90_6
 x_gasoline-grade-90_8 x_gasoline-grade-90_9 x_gasoline-grade-93_1
 x_gasoline-grade-93_3 x_gasoline-grade-93_4 x_gasoline-grade-93_5
 x_gasoline-grade-93_6 x_gasoline-grade-93_8 x_gasoline-grade-93_9
 x_Diesel_1 x_Diesel_3 x_Diesel_4 x_Diesel_5 x_Diesel_6 x_Diesel_8
 x_Diesel_9 x_Engine-Oil_1 x_Engine-Oil_3 x_Engine-Oil_4 x_Engine-Oil_5
 x_Engine-Oil_6 x_Engine-Oil_8 x_Engine-Oil_9
Generals
 Z
End
