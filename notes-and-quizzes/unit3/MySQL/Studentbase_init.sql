CREATE TABLE if not exists(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    FamilyName VARCHAR(255) NOT NULL,
    GivenName VARCHAR(255) NOT NULL,
    YearofGraduation VARCHAR(255) NOT NULL
);

INSERT INTO studentbase (email, FamilyName, GivenName, YearofGraduation) values ("2029.test.matrix@abc.edu.jp","Boi","Bobby","2029");
INSERT INTO studentbase (email, FamilyName, GivenName, YearofGraduation) values ("2030.test.matrix2@def.edu.jp","Salvety","Marine","2030");

SELECT * FROM studentbase; #select everything from the table
SELECT count(*) FROM studentbase; #count the number of rows in the table

SELECT * FROM studentbase order by YearofGraduation; #sort the table by YearofGraduation