-- Person(PersonId, FirstName, LastName)
-- Address(AddressId, PersonId, City, State)

SELECT
  p.FirstName,
  p.LastName,
  a.City,
  a.State
FROM Person AS p
LEFT JOIN Address AS a
  ON p.PersonId = a.PersonId;
