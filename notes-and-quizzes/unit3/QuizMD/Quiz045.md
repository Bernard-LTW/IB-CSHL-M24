# Quiz 045

## Prompt
Download the database smallcase.db from the learning log and write the SQL statements to solve the prompts below.


## Question 1: Create the UML diagram for the database.

![](/Assets/Quiz045_UML.jpeg)
*Fig.1* **UML diagram for the database.**

## Question 2: Create the SQL queries to find the responsible for the fraudulent transaction.

```.sql
SELECT
  CASE
    WHEN total_deposit - total_withdraw != balance THEN 'bad'
    ELSE 'good'
  END AS 'Status',
  total_deposit,
  total_withdraw,
  balance,
  account_id
FROM (
  SELECT
    SUM(amount) AS total_deposit,
    account_id AS a_d
  FROM transactions
  WHERE transaction_type = 'deposit'
  GROUP BY account_id
),
(
  SELECT
    SUM(amount) AS total_withdraw,
    account_id AS a_w
  FROM transactions
  WHERE transaction_type = 'withdraw'
  GROUP BY account_id
),
accounts
WHERE a_d = a_w
  AND a_d = accounts.account_id;
```
 ![](/Assets/Quiz045_EvidenceA.jpg)
*Fig.2* **Image showing results of the query. As we can see from the image above, the responsible parties have account ids of 12, 13, 15, 17, 19 as their account balance doesn't add up after comparing with the according withdrawals and deposits**



## Question 3: What is the name of the customer and the problem that resulted in the bankruptcy of the bank?

```.sql
SELECT customers.first_name, customers.last_name, accounts.account_id
FROM customers
JOIN accounts
ON customers.customer_id = accounts.customer_id
WHERE accounts.account_id IN (12, 13, 15, 17, 19);
```

![](/Assets/Quiz045_EvidenceC.jpg)
*Fig.3* **Image showing results of the query.**

In the image above, we can see that the responsible parties are:
- **Matthew Martin** with account id of 12
- **Ashley Taylor** with account id of 13
- **Nicholas Lewis** with account id of 15
- **David Clark** with account id of 17
- **Daniel Green** with account id of 19





