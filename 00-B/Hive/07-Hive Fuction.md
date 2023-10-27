## Functions in Hive:

1. Mathematical Functions:
    - `ABS()`: returns the absolute value of a number
    - `CEIL()`: returns the smallest integer greater than or equal to a number
    - `FLOOR()`: returns the largest integer less than or equal to a number
    - `ROUND()`: rounds a number to the nearest integer
    - `EXP()`: returns the exponential value of a number
    - `LOG()`: returns the natural logarithm of a number
    - `POWER()`: returns a number raised to a power
    - `SQRT()`: returns the square root of a number
    - `MOD()`: returns the remainder of a division operation

2. String Functions:
    - `CONCAT()`: concatenates two or more strings
    - `SUBSTR()`: returns a substring of a string
    - `LOWER()`: converts a string to lowercase
    - `UPPER()`: converts a string to uppercase
    - `TRIM()`: removes leading and trailing spaces from a string
    - `REPLACE()`: replaces a substring within a string with another substring
    - `REGEXP_REPLACE()`: replaces a pattern within a string with another substring
    - `LENGTH()`: returns the length of a string
    - `INSTR()`: returns the position of a substring within a string
    - `FORMAT()`: formats a string according to a format string

3. Date and Time Functions:
    - `CURRENT_DATE()`: returns the current date
    - `CURRENT_TIMESTAMP()`: returns the current timestamp
    - `DATEDIFF()`: returns the number of days between two dates
    - `DATE_ADD()`: adds a specified number of days to a date
    - `DATE_SUB()`: subtracts a specified number of days from a date
    - `FROM_UNIXTIME()`: converts a Unix timestamp to a date
    - `UNIX_TIMESTAMP()`: returns the Unix timestamp of a specified date
    - `YEAR()`: returns the year of a date
    - `MONTH()`: returns the month of a date
    - `DAY()`: returns the day of a date

4. Conditional Functions:
    - `CASE`: allows for conditional expressions in a query
    - `IF()`: returns one value if a condition is true, and another value if it is false
    - `COALESCE()`: returns the first non-null value in a list of values
    - `NULLIF()`: returns null if two expressions are equal, otherwise returns the first expression

5. Collection Functions:
    - `ARRAY()`: returns an array containing a list of values
    - `MAP()`: returns a map containing key-value pairs
    - `STRUCT()`: returns a struct containing a set of fields

Note that this is not an exhaustive list and there may be additional functions available in your specific Hive environment.

some examples of these functions in use:

1. Mathematical Functions:

```
SELECT 
  ABS(-5), 
  CEIL(3.2), 
  FLOOR(3.8), 
  ROUND(3.456), 
  EXP(2), 
  LOG(10), 
  POWER(2,3), 
  SQRT(16), 
  MOD(10,3);
```
Output: `5 4 3 3 7.3890560989306495 2.302585092994046 8 4 1`

2. String Functions:

```
SELECT 
  CONCAT('Hello ', 'world'), 
  SUBSTR('Hive is awesome', 5, 2), 
  LOWER('THIS IS LOWERCASE'), 
  UPPER('this is uppercase'), 
  TRIM('   remove spaces   '), 
  REPLACE('Hive is awesome', 'is', 'was'), 
  REGEXP_REPLACE('Hive is awesome', 'is|awesome', 'was'), 
  LENGTH('Hive is awesome'), 
  INSTR('Hive is awesome', 'is'), 
  FORMAT('%s %s', 'Hello', 'world');
```
Output: `Hello world is is lowercase THIS IS UPPERCASE remove spaces Hive was awesome Hive was wasome 14 5 Hello world`

3. Date and Time Functions:

```
SELECT 
  CURRENT_DATE(), 
  CURRENT_TIMESTAMP(), 
  DATEDIFF('2022-12-31', '2022-01-01'), 
  DATE_ADD('2022-01-01', 7), 
  DATE_SUB('2022-01-01', 7), 
  FROM_UNIXTIME(1642109400), 
  UNIX_TIMESTAMP('2022-01-01 00:00:00'), 
  YEAR('2022-01-01'), 
  MONTH('2022-01-01'), 
  DAY('2022-01-01');
```
Output: `2022-11-12 2022-11-12 335 2022-01-08 2021-12-25 2022-01-13 1640995200 2022 1 1`

4. Conditional Functions:

```
SELECT 
  CASE 
    WHEN 1 > 2 THEN 'True' 
    ELSE 'False' 
  END AS is_greater, 
  IF(1 > 2, 'True', 'False') AS is_greater_alternate, 
  COALESCE(NULL, 'Hello', NULL, 'world'), 
  NULLIF(1, 2), 
  NULLIF(2, 2);
```
Output: `False False Hello 1 NULL`

5. Collection Functions:

```
SELECT 
  ARRAY(1, 2, 3), 
  MAP('key1', 'value1', 'key2', 'value2'), 
  STRUCT('John', 25), 
  STRUCT('Jane', 30).name;
```
Output: `["1","2","3"] {"key1":"value1","key2":"value2"} {"col1":"John","col2":25} "Jane"`