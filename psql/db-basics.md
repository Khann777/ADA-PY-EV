SQL - (Structured Query  Language/Структурный Язык Запросов) - Язык запросов, который позволяет обращаться и работать с БД (Создание/Чтение/Изменение/Удаление)

БД(База Данных) - Хранилище, в котором хранятся данные

СУБД (Система Управления Базой Данных) - Система которая позволяет полноценно работать с базой данных при помощи SQL (только в SQL-СУБД), существует 2 вида СУБД:
    1. Реляционные(relational) - Реляционная СУБД позволяет связывать таблицы между собой
    2. Не реляционные(non relational) - БД которая не имеет связей, зачастую данные хранятся в паре {ключ: значение}

PostgreSQL - Реляционная СУБД при помощи которой мы будем работаь с базами данных
(PostgreSQL, SQLite, MySQL, итд) - Реляционные
(MongoDB, redis) - Не реляционные

Основные команды PostgreSQL:

-- psql - команда, для того чтобы войти в оболочку Postgres
-- \q - команда, для того чтобы выйти из оболочки Postgres
-- \с <db_name>- команда, для подключения к базе данных
-- \c - если не указать название БД, то выведет сообщение в котором покажет к какой бд мы подключенны, и под каким юзером
-- \l - выведет весь список баз данных
-- \du - выведет список всех пользователей и их прав
-- \dt - выведет все таблицы в текущей бд
-- \d+ - показывает более подробную информацию о таблицах

------------------ТИПЫ ДАННЫХ POSTGRES--------------------------
ЧИСЛОВЫЕ ТИПЫ ДАННЫХ:
- smallint - хранит маленькие числа в диапазоне от -32767 до 32767, занимает 2 байта
- integer - хранит числа в более широком диапазоне, занимает 4 байта
- bigint - хранит огромные числа в диапазоне от -9223372036854775808 до 9223372036854775808, занимает 8 байт
- serial - числовой тип данных, у которого есть автоинкремент

СТРОКОВЫЕ ТИПЫ ДАННЫХ:
- CHAR(CHARACTER(N)) - строковый тип данных, который имеет фиксированную длину указанную в скобках, указывать ограничение обязательно
    ------Пример:
    email CHAR(100)
    davlyat - имя занимает 7 символов, остальные 93 символа будут забиты пробелами
- character varying (VARCHAR(n)) - строковый тип данных, который имеет динамическую длину 
    ------Пример:
    email VARCHAR(100)
    davlyat - не заполняет все 100 символов, а срезает до 7 символов
- text - строковый тип данных у которого произвольная длина

ТИП ДАННЫХ ДЛЯ ДАТЫ И ВРЕМЕНИb:
-- DATE - тип данных для хранения дат, занимает 4 байта памяти
-- TIME - тип данных для хранения времени, от 00:00:00 до 24:00:00, занимает 8 байта
-- DATETIME - тип данных для хранения даты и времени, занимает 8 байт

БУЛЕВЫЕ ТИПЫ ДАННЫХ:
-- true - истина, вместо этого значения, допускается: (t, TRUE, y, yes, 1)
-- false - ложь, вместо этого значения, допускается: (f, FALSE, no, 0)

JSON - тип данных для хранения данных в JSON формате

КОМАНДА ДЛЯ СОЗДАНИЯ БАЗЫ ДАННЫХ:
CREATE DATABASE <db_name>;

КОМАНДА ДЛЯ УДАЛЕНИЯ БАЗЫ ДАННЫХ:
DROP DATABASE <db_name>;

КОМАНДА ДЛЯ СОЗДАНИЯ ТАБЛИЦЫ:
CREATE TABLE <table_name> (
    <column_name> <column_type>,
);

КОМАНДА ДЛЯ УДАЛЕНИЯ ТАБЛИЦЫ:
DROP TABLE <table_name>;

КОМАНДА ДЛЯ ЗАПОЛНЕНИЯ ТАБЛИЦ:
INSERT INTO <table_name> (<column1>, <column2>, ...) VALUES (<value1>, <value2>, ...);

КОМАНДА  ДЛЯ ВЫВОДА ЗАПИСЕЙ ИЗ ТАБЛИЦЫ:
SELECT * FROM <table_name>;

КОМАНДА ДЛЯ УДАЛЕНИЯ ЗАПИСЕЙ ИЗ ТАБЛИЦЫ:
DELETE FROM <table_name>;

КОМАНДА ДЛЯ ОБНОВЛЕНИЯ ВСЕХ ЗАПИСЕЙ В ТАБЛИЦЕ:
UPDATE <table_name> SET <column_name> = <new_value>;

УСЛОВИЯ:
-- WHERE 
    DELETE FROM <table_name> WHERE id=2;
    DELETE FROM <table_name> WHERE email='davlyat.n@gmail.com';
-- LIKE - Выберает все записи у которых в столбце name присутствует 'apple' (LIKE чувствителен к регистру)
    ПРИМЕР:
        SELECT * FROM <table_name> WHERE name like '%apple%';

-- ILIKE - Выберает все записи у которых в столбце name присутствует 'apple' (LIKE не чувствителен к регистру)
    ПРИМЕР:
        SELECT * FROM <table_name> WHERE name ilike '%apple%';

-- ORDER BY - Условие, для сортировки по определенному полю, по дефолту сортирует по возрастанию (ASC - ascending/возрастанию)
    ПРИМЕР:
        SELECT * FROM <table_name> ORDER BY <column>; - Отсортирует по возрастанию все записи в таблице <table_name> по полю <column>

-- ORDER BY - Условие, для сортировки по определенному полю, сортирует по убыванию (DESC - descending/убыванию)
    ПРИМЕР:
        SELECT * FROM <table_name> ORDER BY <column> DESC; - Отсортирует по убыванию все записи в таблице <table_name> по полю <column>

-- LIMIT - Условие,которое позволяет ограничивать выводимое количество записей
    ПРИМЕР:
        SELECT name FROM test_table LIMIT 3; - выведет только 3 записи, но только поля name

-- OFFSET - Условие, которое позволяет пропустить какое-то количество записей
    ПРИМЕР:
        SELECT * FROM test_table OFFSET 3; - сначала пропустит первые 3 записи, а затем выведет все оставшиеся

        КОМБИНАЦИЯ LIMIT/OFFSET:
            SELECT * FROM test_table LIMIT 2 OFFSET 4;

СВЯЗИ PRIMARY KEY и FOREIGN KEY:
    -- PRIMARY KEY (Первичный ключ) (pk) - ключ, ограничение, которое накладывается на поле, которое будет использовано в связях (Это уникальный идентификационный ключ. Зачастую применяется для ID)
    -- FOREIGN KEY (Внешний ключ) (fk) - ключ, ограничение, которое накладывается на поле, которое ссылается на pk (PRIMARY KEY) в другой таблице. (НАПРИМЕР: есть 2 таблицы, таблица passport, и таблица person, и в таблице passport будет поле 'person_id', это будет поле, которое ссылается на поле 'id' в таблице 'person')

ПРИМЕР С ТАБЛИЦАМИ AUTHOR и BOOK:
- CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_name VARCHAR(50)
);
- CREATE TABLE book (
    id SERIAL PRIMARY KEY, 
    title VARCHAR(50),
    author_id INT,

    CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author (id)
);

ВИДЫ СВЯЗЕЙ МЕЖДУ ТАБЛИЦАМИ:
 - One-to-One - Один к одному, 1. Один человек - один паспорт id. 2. Один автор - одна автобиография 
 - One-to-Many - Один к многим,1. Одна категория - много товаров. 2. Один автор - много книг
 - Many-to-Many - Многие к многим. 1. Один учитель - много учеников, один ученик - много учителей (много учителей - много учеников) 2. Один разработчик - много проектов, один проект - много разработчиков ( много разработчиков - много проектов)

 ПРИМЕРЫ СВЯЗЕЙ:
    -- One-to-One
        - CREATE TABLE author (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50)
        );
        - CREATE TABLE authobiography (
            id SERIAL PRIMARY KEY,
            body TEXT,
            author_id INT UNIQUE,

            CONSTRAINT fk_bio_author FOREIGN KEY (author_id) REFERENCES author (id)
        );

    -- Many-to-Many
        - CREATE TABLE developer (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            language VARCHAR(50)
        );

        - CREATE TABLE project (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50),
            tz TEXT
        );

        - CREATE TABLE dev_proj (
            id SERIAL PRIMARY KEY,
            developer_id INT,
            project_id INT,

            CONSTRAINT fk_developer_id FOREIGN KEY (developer_id) REFERENCES developer (id),

            CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES project (id)
        );

JOIN - инструкция, которая позволяет в запросах SELECT выбирать данные из нескольких таблиц сразу.
    ВИДЫ JOIN:
        -- INNER JOIN - достаются только те записи, у которых есть пара (у которых есть связь).
        -- FULL JOIN - достаются все записи из обоих таблиц (в не зависимости от того, есть ли запись или нет).
        -- LEFT JOIN - достаются все записи из левой таблици, и из правой, если есть связь (ПАРА).
        -- RIGHT JOIN - достаются все записи из правой таблици, и из левой, если есть связь (ПАРА).

        * Где 'левая' таблица - та которая пишется до JOIN, 'правая' - та которая пишется после JOIN.

ПРИМЕР 1:

- CREATE TABLE bloger (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

- CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20),
    body TEXT,
    bloger_id INT,
    created_at DATE,

    CONSTRAINT fb_bloger_id FOREIGN KEY (bloger_id) REFERENCES bloger (id)
);

ПРИМЕР 2:

- CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

- CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    title VARCHAR(20),
    price DECIMAL
);

- CREATE TABLE cart (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    product_id INT,

    CONSTRAINT fk_cart_customer FOREIGN KEY (customer_id) REFERENCES customer (id),

    CONSTRAINT fk_cart_product FOREIGN KEY (product_id) REFERENCES product (id)
);

АГРЕГАТНЫЕ ФУНКЦИИ:
    Агрегатные функции - это функции, которые помогают, считать, находить минимум/максимум, складывать и другие вычисления для групп данных.

    ** ДЛЯ РАБОТЫ МНОГИХ АГРЕГАЬНЫХ ФУНКЦИЙ ТРЕБУЕТСЯ ГРУППИРОВКА ЧЕРЕЗ ФУНКЦИЮ GROUP BY

-- COUNT - считает количество записей в сгруппированном поле
    ПРИМЕР:
-- пример из post_blogger_db
- SELECT bloger.name, COUNT(post.id) AS posts_count FROM bloger JOIN post ON bloger.id = post.bloger_id GROUP BY (bloger.name);

-- ARRAY_AGG - объединяет записи сгруппированного поля в массив.
    ПРИМЕР:
-- пример из post_blogger_db
- SELECT bloger.name, ARRAY_AGG(post.title) AS post_titles FROM bloger JOIN post ON bloger.id = post.bloger_id GROUP BY(bloger.name);

-- MIN/MAX -

-- SUM - 