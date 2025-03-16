CREATE TABLE Employees
(
    employee_id INT PRIMARY KEY,
    first_name  VARCHAR(255) NOT NULL,
    last_name   VARCHAR(255) NOT NULL,
    hireDate    DATE         NOT NULL,
    salary      FLOAT        NOT NULL,
    department_id INT NOT NULL
)

CREATE TABLE Bussines_tips
(
    tips_id     INT PRIMARY KEY,
    start_time  DATETIME      NOT NULL,
    end_time    DATETIME      NOT NULL,
    desination  VARCHAR(255)  NOT NULL,
    title       VARCHAR(255)  NOT NULL,
    description VARCHAR(4000) NOT NULL

)
CREATE TABLE Bussines_tips_Employees
(
    employee_id INT FOREIGN KEY REFERENCES Employees(employee_id ),
    tip_id      INT FOREIGN KEY REFERENCES Bussines_tips(tips_id )
)

CREATE TABLE CARS
(
    car_id      INT PRIMARY KEY,
    milage      INT          NOT NULL,
    brand       VARCHAR(100) NOT NULL,
    engine_type VARCHAR(100) NOT NULL,
    employee_id INT FOREIGN KEY REFERENCES Employees(employee_id )
)

CREATE TABLE ADDRESS(
address_id     INT PRIMARY KEY,
street  VARCHAR(255)  NOT NULL,
city       VARCHAR(255)  NOT NULL,
country VARCHAR(255)  NOT NULL,
employee_id INT FOREIGN KEY REFERENCES Employees(employee_id )
)

CREATE TABLE Department(
department  INT PRIMARY KEY,
name VARCHAR(255)
)









