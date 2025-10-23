SELECT c.Name AS Customers
FROM Customers AS c
WHERE NOT EXISTS (
  SELECT 1
  FROM Orders o
  WHERE o.CustomerId = c.Id
);
