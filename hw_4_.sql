-- 1. Виведіть усі можливі пари рядків викладачів і груп.
-- SELECT Teachers.Name AS TeacherName, Teachers.Surname AS TeacherSurname, Groups.Name AS GroupName
-- FROM Teachers, Groups;

-- 2. Виведіть назви факультетів, фонд фінансування кафедр
-- яких перевищує фонд фінансування факультету.
-- SELECT DISTINCT Faculties.Name AS FacultyName
-- FROM Faculties
-- JOIN Departments ON Faculties.Id = Departments.FacultyId
-- WHERE Departments.Financing > Faculties.Financing;

-- 3. Виведіть прізвища кураторів груп і назви груп, які вони
-- курирують.
-- SELECT Curators.Surname AS CuratorSurname, Groups.Name AS GroupName
-- FROM GroupsCurators
-- JOIN Curators ON GroupsCurators.CuratorId = Curators.Id
-- JOIN Groups ON GroupsCurators.GroupId = Groups.Id;


-- 4. Виведіть імена та прізвища викладачів, які читають лекції
-- у групі «P107».
-- SELECT DISTINCT Teachers.Name AS TeacherName, Teachers.Surname AS TeacherSurname
-- FROM GroupsLectures
-- JOIN Lectures ON GroupsLectures.LectureId = Lectures.Id
-- JOIN Teachers ON Lectures.TeacherId = Teachers.Id
-- JOIN Groups ON GroupsLectures.GroupId = Groups.Id
-- WHERE Groups.Name = 'B2';


-- 5. Виведіть прізвища викладачів і назви факультетів, на яких
-- вони читають лекції.
-- SELECT DISTINCT Teachers.Surname AS TeacherSurname, Faculties.Name AS FacultyName
-- FROM Lectures
-- JOIN Teachers ON Lectures.TeacherId = Teachers.Id
-- JOIN Subjects ON Lectures.SubjectId = Subjects.Id
-- JOIN GroupsLectures ON GroupsLectures.LectureId = Lectures.Id
-- JOIN Groups ON GroupsLectures.GroupId = Groups.Id
-- JOIN Departments ON Groups.DepartmentId = Departments.Id
-- JOIN Faculties ON Departments.FacultyId = Faculties.Id;

-- 6. Виведіть назви кафедр і назви груп, які до них належать.
-- SELECT Departments.Name AS DepartmentName, Groups.Name AS GroupName
-- FROM Groups
-- JOIN Departments ON Groups.DepartmentId = Departments.Id;

-- 7. Виведіть назви предметів, які викладає викладач «Samantha
-- Adams».
-- SELECT Subjects.Name AS SubjectName
-- FROM Lectures
-- JOIN Subjects ON Lectures.SubjectId = Subjects.Id
-- JOIN Teachers ON Lectures.TeacherId = Teachers.Id
-- WHERE Teachers.Name = 'Олександр' AND Teachers.Surname = 'Іванов';

-- 8. Виведіть назви кафедр, на яких викладається дисципліна
-- «Database Theory».
-- SELECT DISTINCT Departments.Name AS DepartmentName
-- FROM Lectures
-- JOIN Subjects ON Lectures.SubjectId = Subjects.Id
-- JOIN GroupsLectures ON Lectures.Id = GroupsLectures.LectureId
-- JOIN Groups ON GroupsLectures.GroupId = Groups.Id
-- JOIN Departments ON Groups.DepartmentId = Departments.Id
-- WHERE Subjects.Name = 'Математика 101';

-- 9. Виведіть назви груп, що належать до факультету «Computer
-- Science».
-- SELECT Groups.Name AS GroupName
-- FROM Groups
-- JOIN Departments ON Groups.DepartmentId = Departments.Id
-- JOIN Faculties ON Departments.FacultyId = Faculties.Id
-- WHERE Faculties.Name = 'Факультет хімії';


-- 10. Виведіть назви груп 5-го курсу, а також назви факультетів,
-- до яких вони належать.
-- SELECT Groups.Name AS GroupName, Faculties.Name AS FacultyName
-- FROM Groups
-- JOIN Departments ON Groups.DepartmentId = Departments.Id
-- JOIN Faculties ON Departments.FacultyId = Faculties.Id
-- WHERE Groups.Year = 5;


-- 11. Виведіть повні імена викладачів і лекції, які вони читають
-- (назви предметів та груп). Зробіть відбір по тим лекціям,
-- які проходять в аудиторії «B103»
SELECT Teachers.Name AS TeacherName, Teachers.Surname AS TeacherSurname,
       Subjects.Name AS SubjectName, Groups.Name AS GroupName
FROM Lectures
JOIN Subjects ON Lectures.SubjectId = Subjects.Id
JOIN Teachers ON Lectures.TeacherId = Teachers.Id
JOIN GroupsLectures ON Lectures.Id = GroupsLectures.LectureId
JOIN Groups ON GroupsLectures.GroupId = Groups.Id
WHERE Lectures.LectureRoom = 'Room 104';


