For safety reasons, the major of a small town in England is considering constructing a new soccer stadium to
replace the old one, which is almost a hundred years old. After several negotiation rounds, a local company
was awarded the construction contract with the condition that the stadium is completed as fast as possible.
To complete the construction of the stadium, the company needs to perform the tasks that are listed in the
following table. The duration of the tasks is expressed in weeks. Also, some tasks can only start after the
completion of other tasks.

1. What is the least possible number of weeks required for completing the construction of the stadium?
Formulate an optimization model to solve this problem. Solve it using Gurobi.

2. Suppose that the major of the town is eager to finish the project earlier than the time announced by
the construction company (i.e., the answer for question 1). To achieve this, he is prepared to pay a
bonus of $30K for every week the project is finished earlier. The construction company may employ
additional workers and rent more equipment to cut down on the completion time of some of the tasks.
The table above also provides the maximum number of weeks the company can save per task (column
“Max. speedup.”) and the cost of employing the extra workers and renting additional equipment to
cut down a week time per task (column “Cost per week saved”). Assume that these are fixed charges
per week (i.e., the company cannot pay half the cost to save half a week time). When will the project
be completed if the builder wishes to maximize his profit? Use Gurobi to answer these questions.


          ┌-------------------------------------------------------------------------------------------------┐
          ┆                                                                           Max.   Cost per week  ┆
          ┆  Task        Description                       Duration    Predecessors  speedup    saved ($1K) ┆
          ┆    1         Installing the construction site    2             -           0           -        ┆
          ┆    2         Terracing                           16            1           3           30       ┆
          ┆    3         Constructing the foundations        9             2           1           26       ┆
          ┆    4         Access roads and other networks     8             2           2           12       ┆
          ┆    5         Erecting the basement               10            3           2           17       ┆
          ┆    6         Main floor                          6          4 and 5        1           15       ┆
          ┆    7         Dividing up the changing rooms      2             4           1           8        ┆
          ┆    8         Electrifying the terraces           2             6           0           -        ┆ 
          ┆    9         Constructing the roof               9          4 and 6        2           42       ┆
          ┆    10        Lighting of the stadium             5             4           1           21       ┆
          ┆    11        Installing the terraces             3             6           1           18       ┆
          ┆    12        Sealing the roof                    2             9           0           -        ┆
          ┆    13        Finishing the changing rooms        1             7           0           -        ┆
          ┆    14        Constructing the ticket office      7             2           2           22       ┆
          ┆    15        Secondary access roads              4          4 and 14       2           12       ┆    
          ┆    16        Means of signaling                  3          8, 11,and 14   1           6        ┆
          ┆    17        Lawn and sport accessories          9             12          3           16       ┆
          ┆    18        Handing over the building           1             17          0           -        ┆
          └-------------------------------------------------------------------------------------------------┘
