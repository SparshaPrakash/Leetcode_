-- Person(Id, Email)

DELETE p1
FROM Person AS p1
JOIN Person AS p2
  ON p1.Email = p2.Email   -- same email
 AND p1.Id > p2.Id;        -- p1 is the higher-Id duplicate → delete it
