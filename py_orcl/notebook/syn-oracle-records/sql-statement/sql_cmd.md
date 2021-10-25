



## CREATE

-- create a new table using all the columns and data types
-- from an existing table:
CREATE TABLE T3 AS SELECT * FROM T1 WITH NO DATA;
-- create a new table, providing new names for the columns, but
-- using the data types from the columns of an existing table:
CREATE TABLE T3 (A,B,C,D,E) AS SELECT * FROM T1 WITH NO DATA;
-- create a new table, providing new names for the columns,
-- using the data types from the indicated columns of an existing table:
CREATE TABLE T3 (A,B,C) AS SELECT V,DP,I FROM T1 WITH NO DATA;
-- This example shows that the columns in the result of the
-- query expression may be unnamed expressions, but their data
-- types can still be used to provide the data types for the
-- corresponding named columns in the newly-created table:
CREATE TABLE T3 (X,Y) AS SELECT 2*I,2.0*F FROM T1 WITH NO DATA;

## UPDATE

Oracle / PLSQL: UPDATE Statement
This Oracle tutorial explains how to use the Oracle UPDATE statement with syntax, examples, and practice exercises.

Description
The Oracle UPDATE statement is used to update existing records in a table in an Oracle database. There are 2 syntaxes for an update query in Oracle depending on whether you are performing a traditional update or updating one table with data from another table.

Syntax
The syntax for the UPDATE statement when updating one table in Oracle/PLSQL is:

UPDATE table
SET column1 = expression1,
    column2 = expression2,
    ...
    column_n = expression_n
[WHERE conditions];
OR

The syntax for the Oracle UPDATE statement when updating one table with data from another table is:

UPDATE table1
SET column1 = (SELECT expression1
               FROM table2
               WHERE conditions)
[WHERE conditions];
Parameters or Arguments

## DISTINCT


SELECT COUNT(DISTINCT column(s)) FROM table

## COUNT

SELECT COUNT( * )
FROM agents
HAVING COUNT(*)>3;

SELECT commission, COUNT (*)
FROM agents
GROUP BY commission
HAVING COUNT(*)>3;

## DELETE 

DELETE FROM table_name WHERE condition;

