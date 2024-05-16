-- Для бази даних Академія створіть такі запити:
-- 1. Вивести таблицю кафедр, але розташувати її поля у зворотному порядку.
-- SELECT Financing, Name, Id
-- FROM Departments

-- 2. Вивести назви груп та їх рейтинги з уточненнями до назв
-- полів відповідно до назви таблиці.
-- SELECT NAME AS "Name", Rating AS "Rating"
-- FROM Groups

-- 3. Вивести для викладачів їх прізвища, відсоток ставки по
-- відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).
-- SELECT 
--     Surname AS "Прізвище",
--     (Salary / (Salary + Premium)) * 100 AS "Відсоток ставки до надбавки",
--     (Premium / (Salary + Premium)) * 100 AS "Відсоток ставки до зарплати"
-- FROM Teachers

-- 4. Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
-- SELECT CONCAT('Декан факультету ', Name, ' - це ', Dean) AS "Інформація про факультет"
-- FROM Faculties

-- 5. Вивести прізвища професорів, ставка яких перевищує 1050.
-- SELECT Surname
-- FROM Teachers
-- WHERE IsProfessor = True AND Salary > 1050

-- 6. Вивести назви кафедр, фонд фінансування яких менший,
-- ніж 11000 або більший за 25000.
-- SELECT Name
-- FROM Departments
-- WHERE Financing > 25000 OR Financing < 11000

-- 7. Вивести назви факультетів, окрім факультету «Computer
-- Science».
-- SELECT Name
-- FROM Faculties
-- WHERE Name NOT IN ('Факультет комп''ютерних наук')

-- 8. Вивести прізвища та посади викладачів, які не є професорами.
-- SELECT Surname, Position
-- FROM Teachers
-- WHERE IsProfessor = FALSE

-- 9. Вивести прізвища, посади, ставки та надбавки асистентів,
-- надбавка яких у діапазоні від 160 до 550.
-- SELECT Surname, Position, Salary, Premium
-- FROM Teachers
-- WHERE IsAssistant = TRUE AND Premium BETWEEN 160 AND 550

-- 10. Вивести прізвища та ставки асистентів.
-- SELECT Surname, Salary
-- FROM Teachers
-- WHERE IsAssistant = TRUE

-- 11. Вивести прізвища та посади викладачів, які були прийняті
-- на роботу до 01.01.2000.
-- SELECT Surname, Position
-- FROM Teachers
-- WHERE EmploymentDate < '2000-01-01'

-- 12. Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
-- назвіть «Name of Department».
-- SELECT NAME AS "Name of Department"
-- FROM Departments
-- WHERE NAME < 'Факультет біології'
-- ORDER BY NAME

-- 13. Вивести прізвища асистентів із зарплатою (сума ставки
-- та надбавки) не більше 1200.
-- SELECT Surname
-- FROM Teachers
-- WHERE IsAssistant = True AND (Salary + Premium) <= 1200

-- 14. Вивести назви груп 5-го курсу з рейтингом у діапазоні
-- від 2 до 4.
-- SELECT Name
-- FROM Groups
-- WHERE Year = 5 AND Rating BETWEEN 2 AND 4

-- 15. Вивести прізвища асистентів зі ставкою менше, ніж 550
-- або надбавкою менше, ніж 200.
SELECT Surname
FROM Teachers
WHERE IsAssistant = True AND (Salary < 550 OR Premium < 200)
