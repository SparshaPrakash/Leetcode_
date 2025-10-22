SELECT e.Name AS Employee
FROM Employee AS e
JOIN Employee AS m
  ON e.ManagerId = m.Id         -- match each employee to their manager
WHERE e.Salary > m.Salary;      -- keep only those earning more than their manager
