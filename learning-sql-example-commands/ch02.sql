CREATE TABLE person
 (person_id SMALLINT UNSIGNED,
  fname VARCHAR(20),
  lname VARCHAR(20),
  eye_color CHAR(2),
  birth_date DATE,
  street VARCHAR(30),
  city VARCHAR(20),
  state VARCHAR(20),
  country VARCHAR(20),
  postal_code VARCHAR(20),
  CONSTRAINT pk_person PRIMARY KEY (person_id)
 );

/* mysql version of this table*/
CREATE TABLE person
 (person_id SMALLINT UNSIGNED,
  fname VARCHAR(20),
  lname VARCHAR(20),
  eye_color ENUM('BR','BL','GR'),
  birth_date DATE,
  street VARCHAR(30),
  city VARCHAR(20),
  state VARCHAR(20),
  country VARCHAR(20),
  postal_code VARCHAR(20),
  CONSTRAINT pk_person PRIMARY KEY (person_id)
 );

/* sqlite version of this table*/
CREATE TABLE person
 (person_id INTEGER PRIMARY KEY,
  fname VARCHAR(20),
  lname VARCHAR(20),
  eye_color TEXT CHECK( eye_color In ('BR','BL','GR')),
  birth_date DATE,
  street VARCHAR(30),
  city VARCHAR(20),
  state VARCHAR(20),
  country VARCHAR(20),
  postal_code VARCHAR(20)
 );

CREATE TABLE favorite_food
 (person_id SMALLINT UNSIGNED,
  food VARCHAR(20),
  CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
  CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id)
  REFERENCES person (person_id)
);

/* Will not work or is needed in sqlite as integers declared as primary keys will automatically auto increment */
ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;

INSERT INTO person
  (person_id, fname, lname, eye_color, birth_date)
  VALUES (null, 'William','Turner', 'BR', '1972-05-27');

SELECT person_id, fname, lname, birth_date
  FROM person;

SELECT person_id, fname, lname, birth_date
  FROM person
  WHERE person_id = 1;

SELECT person_id, fname, lname, birth_date
  FROM person
  WHERE lname = 'Turner';

INSERT INTO favorite_food (person_id, food)
VALUES (1, 'pizza');

INSERT INTO favorite_food (person_id, food)
VALUES (1, 'cookies');

INSERT INTO favorite_food (person_id, food)
VALUES (1, 'nachos');

SELECT food
  FROM favorite_food
  WHERE person_id = 1
  ORDER BY food;

INSERT INTO person
(person_id, fname, lname, eye_color, birth_date, street, city, state, country, postal_code)
VALUES (null, 'Susan','Smith', 'BL', '1975-11-02', '23 Maple St.', 'Arlington', 'VA', 'USA', '20220');

SELECT person_id, fname, lname, birth_date
  FROM person;

UPDATE person
  SET street = '1225 Tremont St.',
  city = 'Boston',
  state = 'MA',
  country = 'USA',
  postal_code = '02138'
  WHERE person_id = 1;

DELETE FROM person
  WHERE person_id = 2;


/* Failed statement */
INSERT INTO person
(person_id, fname, lname, eye_color, birth_date)
VALUES (1, 'Charles','Fulton', 'GR', '1968-01-15');

/* Failed statement */
INSERT INTO favorite_food (person_id, food)
  VALUES (999, 'lasagna');

/* Failed statement */
UPDATE person
  SET eye_color = 'ZZ'
  WHERE person_id = 1;

/* Failed statement */
UPDATE person
  SET birth_date = 'DEC-21-1980'
  WHERE person_id = 1;

/* Failed statement */
