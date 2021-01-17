Given the current conditions associated with the COVID-19 pandemic, the epidemiology department at
St. Joseph’s Hospital needs to organize a new working schedule for its nurses. A working day in this
department is subdivided into twelve periods of two hours. The number of nurses that need to be available
during each of these periods is different based on the patient traffic: for example, only a few nurses are
required during the night, whereas this number increases during the morning periods. The following table
list the nurse requirement for every time period.



          ┌-------------------------------------------------------------┐
          ┆ Period    Time interval       Min. number of nurses         ┆
          ┆    1         12AM-2AM                    15                 ┆
          ┆    2         2AM-4AM                     15                 ┆
          ┆    3         4AM-6AM                     15                 ┆
          ┆    4         6AM-8AM                     35                 ┆
          ┆    5         8AM-10AM                    40                 ┆
          ┆    6         10AM-12PM                   40                 ┆
          ┆    7         12PM-2PM                    40                 ┆
          ┆    8         2PM-4PM                     30                 ┆
          ┆    9         4PM-6PM                     31                 ┆
          ┆    10        6PM-8PM                     35                 ┆
          ┆    11        8PM-10PM                    30                 ┆
          ┆    12        10PM-12AM                   20                 ┆
          └-------------------------------------------------------------┘

1. Determine the minimum number of nurses required to cover all the periods, knowing that each nurse
must take a break of two hours after they have worked for four hours. To this end, identify how many
nurses must begin their shifts at each time period. Formulate this problem as an integer program and
solve it using Gurobi.
2. Suppose that because of the crisis, the department has only 80 nurses available to cover all the periods,
which is insufficient given the requirements. For this reason, the head of the department proposes that
part of the nurses works for two additional hours followed immediately the last four hours of their
shift without having an extra break. Determine a valid schedule that minimizes the number of nurses
working overtime. Solve the problem using Gurobi
