DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;


CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);

INSERT INTO cohorts (name, starting_date ) VALUES ('Andrew1', '2023-10-06');
INSERT INTO cohorts (name, starting_date ) VALUES ('Andrew2', '2023-10-07');
INSERT INTO cohorts (name, starting_date ) VALUES ('Andrew3', '2023-10-08');
INSERT INTO cohorts (name, starting_date ) VALUES ('Andrew4', '2023-10-09');

INSERT INTO students (name, cohort_id ) VALUES ('Andrew1', 1);
INSERT INTO students (name, cohort_id ) VALUES ('Andrew2', 2);
INSERT INTO students (name, cohort_id ) VALUES ('Andrew3', 3);
INSERT INTO students (name, cohort_id ) VALUES ('Andrew4', 4);

