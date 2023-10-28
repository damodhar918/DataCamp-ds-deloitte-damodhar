# Hive Developer Guide: Aggregate Functions

Aggregate functions are the most frequently used built-in functions in Hive. They take a set of values and return a single value. When used with a group, they aggregate all values in each group and return one value for each group.

In Hive, aggregate functions can be used with or without GROUP BY functions. However, these aggregation functions are mostly used with GROUP BY. Let's take a look at some examples of how to use aggregation functions with and without applying groups.

## Hive Aggregate Functions List

Here's a list of the common Hive aggregate functions:

| Function      | Syntax                                 | Description                                                                                                                                                  |
| ------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| COUNT()       | COUNT(\*)<br/>COUNT(\[DISTINCT\] expr) | Returns the count of all rows in a table (including NULL values). When you specify a column as an input, it ignores NULL values in the column for the count. |
| SUM()         | SUM(col)<br/>SUM(DISTINCT col)         | Returns the sum of all values in a column. When used with a group, it returns the sum for each group.                                                        |
| AVG()         | AVG(col)<br/>AVG(DISTINCT col)         | Returns the average of all values in a column. When used with a group, it returns an average for each group.                                                 |
| MIN()         | MIN(col)                               | Returns the minimum value of the column from all rows. When used with a group, it returns a minimum for each group.                                          |
| MAX()         | MAX(col)                               | Returns the maximum value of the column from all rows. When used with a group, it returns a maximum for each group.                                          |
| VARIANCE()    | VARIANCE(col)<br/>VAR_POP(col)         | Returns the variance of a numeric column for all rows or for each group.                                                                                     |
| VAR_SAMP()    | VAR_SAMP(col)                          | Returns the unbiased sample variance of a numeric column or for each group.                                                                                  |
| STDDEV_POP()  | STDDEV_POP(col)                        | Returns the statistical standard deviation of all values in a column or for each group.                                                                      |
| STDDEV_SAMP() | STDDEV_SAMP(col)                       | Returns the sample statistical standard deviation of all values in a column or for each group.                                                               |
| COVAR_POP()   | COVAR_POP(col1, col2)                  | Returns the population covariance of a pair of numeric columns for all rows or for each group.                                                               |
| COVAR_SAMP()  | COVAR_SAMP(col1, col2)                 | Returns the sample covariance of a pair of numeric columns for all rows or for each group.                                                                   |
| CORR()        | CORR(col1, col2)                       | Returns the Pearson coefficient of correlation of a pair of a numeric columns in the group.                                                                  |

## Hive Aggregate Function Examples:

### COUNT

**Syntax:**

```
COUNT(\*) - Returns the count of all rows in a table (including NULL values).
COUNT(expr) - Returns the total number of rows for expression excluding null.
COUNT(DISTINCT expr[, expr]) - Returns the count of distinct rows of expression (or expressions) excluding null values.
```

**Example:**

```
SELECT COUNT(*) FROM employee;
SELECT COUNT(salary) FROM employee;
SELECT COUNT(DISTINCT gender, salary) FROM employee;
```

### SUM

**Syntax:**

```
SUM(col)
SUM(DISTINCT col)
```

**Example:**

```
SELECT SUM(salary) FROM employee;
SELECT SUM(DISTINCT salary) FROM employee;
SELECT age, SUM(salary) FROM employee GROUP BY age;
```

### AVG

**Syntax:**

```
AVG(col)
AVG(DISTINCT col)
```

**Example:**

```
SELECT AVG(salary) FROM employee;
SELECT AVG(DISTINCT salary) FROM employee;
SELECT age, AVG(salary) FROM employee GROUP BY age;
```

### MIN

**Syntax:**

```
MIN(col)
```

**Example:**

```
SELECT MIN(salary) FROM employee;
```

### MAX

**Syntax:**

```
MAX(col)
```

**Example:**

```
SELECT MAX(salary) FROM employee;
```

### VARIANCE, VAR_POP

**Syntax:**

```
VARIANCE(col)
VAR_POP(col)
```

**Example:**

```
SELECT VARIANCE(salary) FROM employee;
SELECT VAR_POP(salary) FROM employee;
```

### VAR_SAMP

**Syntax:**

```
VAR_SAMP(col)
```

**Example:**

```
SELECT VAR_SAMP(salary) FROM employee;
```

### STDDEV_POP

**Syntax:**

```
STDDEV_POP(col)
```

**Example:**

```
SELECT STDDEV_POP(salary) FROM employee;
```

### STDDEV_SAMP

**Syntax:**

```
STDDEV_SAMP(col)
```

**Example:**

```
SELECT STDDEV_SAMP(salary) FROM employee;
```

### COVAR_POP

**Syntax:**

```
COVAR_POP(col1, col2)
```

**Example:**

```
SELECT COVAR_POP(salary, age) FROM employee;
```

### COVAR_SAMP

**Syntax:**

```
COVAR_SAMP(col1, col2)
```

**Example:**

```
SELECT COVAR_SAMP(salary, age) FROM employee;
```

### CORR

**Syntax:**

```
CORR(col1, col2)
```

**Example:**

```
SELECT CORR(salary, age) FROM employee;
```

## Hive Aggregate Functions with GROUP BY

### collect_set(col)

Collapse the records by group and convert them into an array. Returns a set of objects with duplicate elements eliminated.

#### Example:

```sql
select gender, collect_set(age) from employee group by gender;
```

### collect_list(col)

Collapse the records by group and convert them into an array. Returns a list of objects with duplicates.

#### Example:

```sql
select gender, collect_list(age) from employee group by gender;
```

### variance(col), var_pop(col)

Return the statistical variance of a column in a group.

#### Example:

```sql
select variance(salary) from employee;
```

```sql
select var_pop(salary) from employee;
```

### var_samp(col)

Return the statistical variance of a column in a group.

#### Example:

```sql
select var_samp(salary) from employee;
```

### stddev_pop(col)

Get the standard deviation of a column. Returns the statistical standard deviation of numeric column values provided in the group.

#### Example:

```sql
select stddev_pop(salary) from employee;
```

### stddev_samp(col)

Get the standard deviation of a column. Returns the statistical standard deviation of numeric column values provided in the group.

#### Example:

```sql
select stddev_samp(salary) from employee;
```

## Conclusion

In this cheatsheet, we have covered some useful aggregation functions that every Hive developer must know. These functions help in summarizing the data and generate insights from it.

## Conclusion

These are the most common aggregate functions in Hive and can be used in your queries to perform basic calculations on your data. By using them with GROUP BY clauses, you can aggregate data for each group. Remember that most of these functions ignore NULL values.
