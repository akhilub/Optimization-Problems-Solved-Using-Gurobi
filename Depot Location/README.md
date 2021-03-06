A large company wishes to open new depots to deliver to its sales centers. Every new set-up of a depot has
a fixed cost. Goods are delivered from a depot to the sales centers close to the site. Every delivery has a cost
that depends on the distance covered. The two sorts of cost are quite different: set-up costs are capital costs
which may usually be written off over several years, and transportation costs are operating costs.
There are 12 sites available for the construction of new depots and 12 sales centers need to receive
deliveries from these depots. The following table gives the costs (in thousand $) of satisfying the entire
demand of each customer (sales center) from a depot (not the unit costs). So, for instance, the cost per
unit of supplying customer 9 (who has a total demand of 30 tons according to the table) from depot 1 is $
60,000/30, i.e. $2,000. Certain deliveries that are impossible are marked with the infinity symbol.



          ┌---------------------------------------------------------------┐
          ┆Depot/Customer  1   2   3   4   5   6   7   8   9   10  11  12 ┆
          ┆       1        100 80  50  50  60  100 120 90  60  70  65  110┆
          ┆       2        120 90  60  70  65  110 140 110 80  80  75  130┆
          ┆       3        140 110 80  80  75  130 160 125 100 100 80  150┆
          ┆       4        160 125 100 100 80  150 190 50  130 --  --  -- ┆
          ┆       5        190 150 130 --  --  --  200 180 150 --  --  -- ┆
          ┆       6        200 180 150 --  --  --   100 80 50  50  60  100┆
          ┆       7        100 80  50  50  60  100 120 90  60  70  65  100┆
          ┆       8        120 90  60  70  65  110 140 110 80  80  72  130┆
          ┆       9        140 110 80  80  75  130 160 125 100 100 80  150┆
          ┆       10       160 125 100 100 80  150 190 150 130 --  --  -- ┆
          ┆       11       190 150 130 --  --  --  200 180 150 --  --  -- ┆
          ┆       12       200 180 150 --  --  --  100 80  50  50  60  100┆
          └---------------------------------------------------------------┘
          
          
In addition, for every depot we have the following information: the fixed cost for constructing the depot
that needs to be included into the objective function and its capacity limit, the quantities demanded by the
sales centers (customers), are summarized in the following tables listed below.


          ┌-----------------------------------------------------------------------------------┐
          ┆ Depot    1     2     3      4     5     6     7     8     9     10     11    12   ┆
          ┆ Cost     3,500 9,000 10,000 4,000 3,000 9,000 9,000 3,000 4,000 10,000 9,000 3,500┆
          ┆ Capacity 300   250   100    180   275   300   200   220   270   250    230   180  ┆
          └-----------------------------------------------------------------------------------┘


          ┌-----------------------------------------------------┐
          ┆  Customer 1   2  3  4   5   6   7  8  9  10  11  12 ┆
          ┆  Demand   120 80 75 100 110 100 90 60 30 150 95 120 ┆
          └-----------------------------------------------------┘


In every case, the demand of a customer needs to be satisfied but a sales center may be delivered to from
several depots. Which depots should be opened to minimize the total cost of construction and of delivery,
whilst satisfying all demands? Propose a formulation for this problem. Solve the problem using Gurobi.



