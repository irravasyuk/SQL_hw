-- CREATE TABLE Departments (
-- 	Id SERIAL PRIMARY KEY,
-- 	Financing DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
-- 	Name VARCHAR(100) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0)
-- );
-- INSERT INTO Departments (Financing, Name) VALUES 
--     (50000.00, 'Кафедра комп''ютерних наук'),
--     (75000.00, 'Кафедра математики'),
--     (62000.00, 'Кафедра фізики'),
--     (58000.00, 'Кафедра хімії'),
--     (43000.00, 'Кафедра біології');

-- CREATE TABLE Faculties (
-- 	Id SERIAL PRIMARY KEY,
-- 	Dean VARCHAR(255) NOT NULL CHECK (CHAR_LENGTH(Dean) > 0),
-- 	Name VARCHAR(100) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0)
-- );

-- INSERT INTO Faculties (Dean, Name) VALUES 
--     ('Петро Іванович', 'Факультет комп''ютерних наук'),
--     ('Олена Петрівна', 'Факультет математики'),
--     ('Ігор Сергійович', 'Факультет фізики'),
--     ('Марія Василівна', 'Факультет хімії'),
--     ('Андрій Миколайович', 'Факультет біології');

-- CREATE TABLE Groups (
-- 	Id SERIAL PRIMARY KEY,
-- 	Name VARCHAR(10) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0),
-- 	Rating INT NOT NULL CHECK (Rating BETWEEN 0 AND 5),
-- 	Year INT NOT NULL CHECK (Year BETWEEN 1 AND 5)
-- );

-- INSERT INTO Groups (Name, Rating, Year) VALUES 
--     ('A1', 5, 1),
--     ('B2', 4, 2),
--     ('C3', 3, 3),
--     ('D4', 2, 4),
--     ('E5', 1, 5);

CREATE TABLE Teachers (
	Id SERIAL PRIMARY KEY,
	EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= '1990-01-01'),
	IsAssistant BOOLEAN NOT NULL DEFAULT FALSE,
	IsProfessor BOOLEAN NOT NULL DEFAULT FALSE,
	Name VARCHAR NOT NULL CHECK (CHAR_LENGTH(Name) > 0),
	Position VARCHAR NOT NULL CHECK (CHAR_LENGTH(Position) > 0),
	Premium DECIMAL(10, 2) NOT NULL CHECK (Premium >= 0) DEFAULT 0,
	Salary DECIMAL(10, 2) NOT NULL CHECK (Salary > 0),
	Surname VARCHAR NOT NULL CHECK (CHAR_LENGTH(Surname) > 0)
);

INSERT INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname) VALUES 
    ('2000-05-15', FALSE, TRUE, 'Олександр', 'Професор', 5000.00, 30000.00, 'Іванов'),
    ('2010-09-01', TRUE, FALSE, 'Марія', 'Асистент', 2000.00, 15000.00, 'Петрова'),
    ('2015-03-12', FALSE, FALSE, 'Сергій', 'Лектор', 1000.00, 20000.00, 'Сидоров'),
    ('1995-07-20', TRUE, TRUE, 'Ірина', 'Доцент', 3000.00, 25000.00, 'Коваленко'),
    ('2020-11-10', FALSE, FALSE, 'Анна', 'Асистент', 1500.00, 12000.00, 'Мельник');
