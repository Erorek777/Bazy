USE AdventureWorks2014
SELECT * FROM Person.Person
-- inna wersja tego samego
USE master
SELECT * FROM  AdventureWorks2014.Person.Person

SELECT ProductID, Color, Name,  ProductNumber
FROM Production.Product
ORDER BY Color DESC, Name ASC

SELECT ProductID, Name, Color FROM Production.Product
WHERE color = 'Black'



-- yyy-MM-dd HH:mm:ss:millis
SELECT SellStartDate, Name, Color FROM Production.Product
WHERE SellStartDate = '2008-04-30 00:00:00'


SELECT ProductID, Name, Color FROM Production.Product
WHERE ProductID <= 317

SELECT ProductID, Name, Color FROM Production.Product
WHERE Color != 'black' --<> różny


SELECT ProductID, Name, Color FROM Production.Product
WHERE Color LIKE 'b%' --<> różny

SELECT ProductID, Name, Color FROM Production.Product
WHERE Name LIKE 'Half-Finger Glove, _' -- jeden dowolny

SELECT ProductID, Name, Color FROM Production.Product
WHERE Color = 'black' OR Color = 'red' --lub
--AND
-- OR  - uwaga wykluczający się

SELECT ProductID, Name, Color FROM Production.Product
WHERE (Color = 'black' OR Color = 'red') AND ProductSubcategoryID =14
--AND wykonuje się przed OR

-- SELECT ProductSubcategoryID, Name, Color FROM Production.Product
-- WHERE ProductSubcategoryID = 14 AND NOT Color 'Black'

SELECT ProductID, Name, Color FROM Production.Product
WHERE Color IN ('black', 'Blue', 'Red')

SELECT ProductSubcategoryID, Name, Color FROM Production.Product
WHERE ProductSubcategoryID >= 10

SELECT ProductSubcategoryID, Name, Color FROM Production.Product
WHERE ProductSubcategoryID BETWEEN 10 AND 19

SELECT ProductSubcategoryID, SellStartDate, Name, Color FROM Production.Product
WHERE ProductSubcategoryID BETWEEN '2011-05-31' AND '2011-05-30'


SELECT ProductSubcategoryID, SellStartDate, Name, Color FROM Production.Product
WHERE ProductSubcategoryID BETWEEN '2011-05-31' AND '2011-05-30'

--Null
SELECT ProductSubcategoryID, SellStartDate, Name, Color
FROM Production.Product
WHERE Color IS NULL   -- WHERE Color IS NOT NULL

--TSQL inna notacja
SELECT Name, Color, ISNULL(Color, 'not color') AS SuperColor
FROM Production.Product

--unikatowe kolory
SELECT DISTINCT Color FROM Production.Product

-- nazwa ze spacją wyświetla
SELECT Name AS new_name, Color AS [new color] FROM Production.Product

-- pierwsze 10 wartości
SELECT TOP 10 Name AS new_name, Color AS [new color] FROM Production.Product
SELECT TOP 10 PERCENT Name AS new_name, Color AS [new color] FROM Production.Product
-- lub
-- SELECT Name AS new_name, Color AS [new color] FROM Production.Product Limit 10

-- konkatenacja
SELECT FirstName, LastName, FirstName + '' + LastName AS FullName
FROM Person.Person

-- T-SQL /Jest tylko kompatybilne z Microsoftem
SELECT FirstName,
       LEFT(FirstName, 1) AS FirstLatter,
       LEFT(FirstName, 3) AS First3Latter,
       RIGHT(FirstName, 1) AS LastLatter,
       SUBSTRING(FirstName, 1, 2),
       SUBSTRING(FirstName, 1, 4)
FROM Person.Person

SET LANGUAGE 'Polish' --włądza język polski
-- T-SQL /Jest tylko kompatybilne z Microsoftem

SELECT SellStartDate,
       Year(SellStartDate)AS Year,
       DATENAME(mm, SellStartDate) AS Month,
       DAY(SellStartDate),
       DATEDIFF(yy, SellStartDate, GETDATE()) --aktualna data

FROM Production.Product

-- Select Name, Color, ProductSubCategoryID
-- FROM Production.Product
--         INNER JOIN Production.ProductSubCategory
--                 ON Production.Product.ProductSubCategoryID = Production.Product.ProductSubCategoryID

-- wersja na aliasach
-- psc - klucz obcy
Select p.Name,Color,psc.Name
FROM Production.Product p
 JOIN Production.ProductSubCategory psc
        ON p.ProductSubCategoryID = psc.ProductSubCategoryID
 JOIN ProductCategory pc
        ON psc.ProductCategoryID = pc.ProductCategoryID
WHERE YEAR(p.SellStartDate)> 2010

Select p.Name,p.Color,psc.Name, pc.Name
FROM Production.Product p
 JOIN Production.ProductSubCategory psc
        ON p.ProductSubCategoryID = psc.ProductSubCategoryID
 JOIN ProductCategory pc
        ON psc.ProductCategoryID = pc.ProductCategoryID
WHERE pc.Name Like '%Clo'
ORDER BY psc.Name desc --38 lini


SELECT p.Name, p.ProductSubcategoryID, psc.Name
FROM Production.Product p
        RIGHT JOIN Production.ProductSubcategory psc
        ON p.ProductSubcategoryID = psc.ProductSubcategoryID



-- Grupowanie funkcje agreujące

SELECT COUNT(*) AS ProductCnt,
       COUNT(ProductSubcategoryID) AS Subcategories,
       AVG(Weight) AS AvgWeight,
       Min(Weight) AS MinWeight

FROM Production.Product
SELECT Color, COUNT(*)
FROM Production.Product
GRUP BY Color
GRUP BY Color



SELECT p.Color, COUNT(*)
FROM Production.Product p
    INNER JOIN Production.ProductSubcategory psc ON p.ProductSubcategoryID = psc.ProductSubcategoryID
WHERE  p.Color IS NOT NULL --!=<>
GROUP BY p.Color, psc.Name
HAVING COUNT(*) > 10
ORDER BY p.Color








USE krmazurb

