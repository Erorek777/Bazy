USE krmazurb

SELECT DB_Name()

CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL
)

SELECT * FROM Customers

DROP TABLE Customers --usuwnie

SELECT * FROM Customers

CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    WrongColumnName DATE
)

ALTER TABLE Customers DROP COLUMN WrongColumnName --usuwanie kolumny
ALTER TABLE Customers ADD new_column INT NOT NULL -- dodawanie kolumny

EXEC sp_rename 'Customers.new_column', 'changed_column', 'COLUMN' -- zmiana nazwy

ALTER TABLE Customers DROP COLUMN changed_column

--INSERT

INSERT INTO Customers (customer_id, first_name, birth_date)
VALUES (1, 'Andrzej', '2000-01-01')

INSERT INTO Customers (customer_id, first_name, birth_date)
VALUES (2, 'Michał', '2000-01-01')

DELETE FROM Customers --WHERE Customers

TRUNCATE TABLE Customers  -- Szybkie usuwanie całych stron

CREATE TABLE Test(
    ID INT PRIMARY KEY,
    col_2 INT NULL,
    col_3 INT NULL,
)

INSERT INTO Test (ID, col_2, col_3)
VALUES (2, null, 1)

INSERT INTO Test (ID, col_3)
VALUES (3, 1)

INSERT INTO Test (ID, col_3)
VALUES (3, null)   -- nie przyjmuke wartosci 3

CREATE SCHEMA soltest


CREATE TABLE Customers(
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
)

INSERT INTO Customers (customer_id, first_name, birth_date)
VALUES (1, 'Andrzej', '2000-01-01')

INSERT INTO Customers (customer_id, first_name, birth_date)
VALUES (2, 'Michał', '2000-01-01')

DELETE FROM Customers WHERE customer_id = 2

CREATE TABLE Orders(
    order_id INT PRIMARY KEY IDENTITY,
    order_date DATE NOT NULL,
    customer_id INT FOREIGN KEY REFERENCES Customers(customer_id)
    )

CREATE TABLE Orders(
    order_id INT PRIMARY KEY IDENTITY,
    order_date DATE NOT NULL,
    order_fk_customer_id INT
    )
-- ALTER zmiana tabeli
ALTER TABLE Orders
  ADD CONSTRAINT FK_Orders_Customers_customer_id FOREIGN KEY(order_fk_customer_id)
  REFERENCES Customers(customer_id)


DROP TABLE ORDERS

INSERT INTO Customers (first_name, birth_date)
VALUES (1, 'Andrzej', '2000-01-01')

INSERT INTO Customers (first_name, birth_date)
VALUES (2, 'Michał', '2000-01-01')

INSERT INTO Customers (first_name, birth_date)
VALUES ('2000-01-01', 1)

INSERT INTO Customers (first_name, birth_date)
VALUES (GETDATE(), 10)

DELETE FROM Customers WHERE custumer_id = 1


--usuwanie kaskadowe

ALTER TABLE Orders
  ADD CONSTRAINT FK_Orders_Customers_customer_id FOREIGN KEY(order_fk_customer_id)
  REFERENCES Customers(customer_id)
        ON DELETE CASCADE --usuwanie kaskadowe
        ON DELETE SET NULL -- czasami zmiana na null wystarczy

DELETE FROM Customers WHERE customers_id = 1



ALTER TABLE Customers
ADD CONSTRAINT DF_birth_date DEFAULT GETDATE() FOR birth_date


























