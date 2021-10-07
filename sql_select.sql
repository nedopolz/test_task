SELECT distinct
    date,
    pos,
    sum(loan_amount) OVER (partition by date, pos)
FROM report
ORDER BY date, pos;
/*assuming the following table structure
   id |    date    | pos | loan_amount
----+------------+-----+-------------
  1 | 2021-10-05 |   1 |        1234
  2 | 2021-10-05 |   1 |        1234
  3 | 2021-10-05 |   2 |       21342
  4 | 2021-10-06 |   1 |        1000
  5 | 2021-10-06 |   1 |        2000
*/