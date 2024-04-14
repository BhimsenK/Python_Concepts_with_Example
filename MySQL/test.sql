-- Active: 1713082277420@@127.0.0.1@3306@information_schema
show DATABASES;


#creating a database
create DATABASE if not EXISTS GenAI;

use GenAI;

CREATE TABLE GenAI_course (student INT(10), Name VARCHAR(15), class VARCHAR(20));

select * from GenAI_course;

use GenAI;

show TABLES;

INSERT INTO GenAI_course VALUES (2, "Aditya", "GenAI");

SELECT * FROM GenAI_course;



use GenAI;
create table IF NOT EXISTS GenAI.GenAI_course_data(col1 INT(10) ,col2 float(10,5),col3 float(10,5) ,col4 float(10,5) , col5 float(10,5),col6 float(10,5) ,clo7 float(10,5) , col8 float(10,5) , col9 float(10,5) , col10 float(10,5) , col11 INT(10))

insert into GenAI.GenAI_course_data values(1,1.52101,13.64,4.49,1.10,71.78,0.06,8.75,0.00,0.00,1)

select * from GenAI_new_data;

