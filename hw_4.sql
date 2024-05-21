-- CREATE TABLE Curators (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR NOT NULL CHECK (CHAR_LENGTH(Name) > 0),
--     Surname VARCHAR NOT NULL CHECK (CHAR_LENGTH(Surname) > 0)
-- );

-- INSERT INTO Curators (Name, Surname) VALUES
-- ('Олександр', 'Іванов'),
-- ('Марія', 'Петрова'),
-- ('Сергій', 'Сидоров'),
-- ('Ірина', 'Коваленко'),
-- ('Анна', 'Мельник');

-- CREATE TABLE Departments (
-- 	Id SERIAL PRIMARY KEY,
-- 	Financing DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
-- 	Name VARCHAR(100) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0),
-- 	FacultyId INT NOT NULL
-- );
-- INSERT INTO Departments (Name, Financing, FacultyId) VALUES
-- ('Кафедра комп''ютерних наук', 50000.00, 1),
-- ('Кафедра математики', 40000.00, 2),
-- ('Кафедра фізики', 30000.00, 3),
-- ('Кафедра хімії', 20000.00, 4),
-- ('Кафедра біології', 15000.00, 5);

-- CREATE TABLE Faculties (
--     Id SERIAL PRIMARY KEY,
--     Financing DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0)
-- );

-- INSERT INTO Faculties (Name, Financing) VALUES
-- ('Факультет комп''ютерних наук', 100000.00),
-- ('Факультет математики', 80000.00),
-- ('Факультет фізики', 75000.00),
-- ('Факультет хімії', 70000.00),
-- ('Факультет біології', 65000.00);

-- CREATE TABLE Groups (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(10) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0),
--     Year INT NOT NULL CHECK (Year >= 1 AND Year <= 5),
--     DepartmentId INT NOT NULL
-- );

-- INSERT INTO Groups (Name, Year, DepartmentId) VALUES
-- ('A1', 1, 1),
-- ('B2', 2, 2),
-- ('C3', 3, 3),
-- ('D4', 4, 4),
-- ('E5', 5, 5);

-- CREATE TABLE GroupsCurators (
--     Id SERIAL PRIMARY KEY,
--     CuratorId INT NOT NULL,
--     GroupId INT NOT NULL,
--     FOREIGN KEY (CuratorId) REFERENCES Curators(Id),
--     FOREIGN KEY (GroupId) REFERENCES Groups(Id)
-- );

-- INSERT INTO GroupsCurators (CuratorId, GroupId) VALUES
-- (1, 1),
-- (2, 2),
-- (3, 3),
-- (4, 4),
-- (5, 5);

CREATE TABLE GroupsLectures (
    Id SERIAL PRIMARY KEY,
    GroupId INT NOT NULL,
    LectureId INT NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES Groups(Id),
    FOREIGN KEY (LectureId) REFERENCES Lectures(Id)
);

INSERT INTO GroupsLectures (GroupId, LectureId) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- CREATE TABLE Lectures (
--     Id SERIAL PRIMARY KEY,
--     LectureRoom VARCHAR NOT NULL CHECK (CHAR_LENGTH(LectureRoom) > 0),
--     SubjectId INT NOT NULL,
--     TeacherId INT NOT NULL,
--     FOREIGN KEY (SubjectId) REFERENCES Subjects(Id),
--     FOREIGN KEY (TeacherId) REFERENCES Teachers(Id)
-- );

-- INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
-- ('Room 101', 1, 1),
-- ('Room 102', 2, 2),
-- ('Room 103', 3, 3),
-- ('Room 104', 4, 4),
-- ('Room 105', 5, 5);

-- CREATE TABLE Subjects (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE CHECK (CHAR_LENGTH(Name) > 0)
-- );

-- INSERT INTO Subjects (Name) VALUES
-- ('Комп''ютерні науки 101'),
-- ('Математика 101'),
-- ('Фізика 101'),
-- ('Хімія 101'),
-- ('Біологія 101');

-- CREATE TABLE Teachers (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR NOT NULL CHECK (CHAR_LENGTH(Name) > 0),
--     Salary DECIMAL(10, 2) NOT NULL CHECK (Salary > 0),
--     Surname VARCHAR NOT NULL CHECK (CHAR_LENGTH(Surname) > 0)
-- );

-- INSERT INTO Teachers (Name, Surname, Salary) VALUES
-- ('Олександр', 'Іванов', 30000.00),
-- ('Марія', 'Петрова', 15000.00),
-- ('Сергій', 'Сидоров', 20000.00),
-- ('Ірина', 'Коваленко', 25000.00),
-- ('Анна', 'Мельник', 12000.00);
