create database pdf_files;

use pdf_files;

create table pdfs (id INT(11) NOT NULL auto_increment, name VARCHAR(255),data LONGBLOB NOT NULL, user_name VARCHAR(100), year VARCHAR(100), dept VARCHAR(100),primary key(id));

select * from pdfs;

