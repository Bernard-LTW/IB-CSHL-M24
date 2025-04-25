# Quiz 043

## Prompt
Create a table according to the image and insert two items into the table.

## Code Structure

### SQL Script
```.sql
DROP TABLE if exists Movies;
CREATE TABLE if not exists Movies(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    filmname TEXT,
    yearofprod INTEGER NOT NULL,
    producer VARCHAR(255) NOT NULL,
    director VARCHAR(255) NOT NULL,
    budget INTEGER NOT NULL,
    category VARCHAR(255) NOT NULL
);

INSERT into Movies (filmname, yearofprod, director, producer, budget, category) VALUES ('La La Land', 2016, 'Damien Chazelle', 'Fred Berger', 30000000, 'Musical');
INSERT into Movies (filmname, yearofprod, director, producer, budget, category) VALUES ('The Wolf of Wall Street', 2013, 'Martin Scorsese', 'Martin Scorsese', 100000000, 'Biography');
```

## Evidence

![](/Assets/Quiz043_Evidence.jpg)
*Fig.1* **Image showing GUI of program**

