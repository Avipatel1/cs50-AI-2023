
DROP TABLE IF EXISTS stars_s;
CREATE TABLE stars_s (
	person_id INT,
	movie_id INT,
	FOREIGN KEY (movie_id) REFERENCES movies_s(movie_id),
	FOREIGN KEY (person_id) REFERENCES people_s(person_id)
);

DROP TABLE IF EXISTS people_s;
CREATE TABLE people_s (
	person_id INT PRIMARY KEY,
	person_name VARCHAR(100),
	birth_year INT
);

DROP TABLE IF EXISTS movies_s;
CREATE TABLE movies_s (
	movie_id INT PRIMARY KEY,
	movie_name VARCHAR(100),
	movie_year INT
);

SELECT * FROM stars_s