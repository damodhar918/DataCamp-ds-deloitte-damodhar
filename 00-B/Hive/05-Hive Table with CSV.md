# Introduction to Apache Hive

Apache Hive is a data warehousing application designed for Hadoop, enabling SQL-based querying and analysis of big datasets stored in Hadoop's Distributed File System (HDFS). It provides an SQL-like syntax, called HiveQL, which is used to query and manipulate the data stored in Hadoop.

In this guide, we'll cover some of the basic concepts and commands used in Apache Hive, along with some examples to help you get started.

## Basic Concepts in Apache Hive

### Table Definition

In Apache Hive, a table is defined using the `CREATE TABLE` command followed by the table name and its columns, along with their data types and other properties such as partitioning and storage format.

Example:

```sql
CREATE TABLE employee (
   emp_id INT,
   emp_name STRING,
   emp_salary FLOAT,
   dept_name STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ',';
```

This creates a table called `employee` with columns `emp_id`, `emp_name`, `emp_salary` and `dept_name`. The table is stored in delimited text format with fields separated by a comma.

### Loading Data

Once a table is created, data can be loaded into it using the `LOAD DATA` command or by using an external script.

Example:

```sql
LOAD DATA INPATH '/user/hive/employee_data.csv' INTO TABLE employee;
```

This loads the data from the CSV file located in `/user/hive` directory to the `employee` table created earlier.

### Querying Data

Data in Hive can be queried using the `SELECT` statement, similar to traditional SQL. HiveQL also supports a wide range of functions to manipulate data.

Example:

```sql
SELECT emp_name, emp_salary 
FROM employee 
WHERE dept_name='Sales' 
ORDER BY emp_salary DESC 
LIMIT 10;
```

This query selects the `emp_name` and `emp_salary` columns from the `employee` table where the `dept_name` is 'Sales', orders them by salary in descending order and limits the rows returned to 10.

### Partitioning

Partitioning is a way of dividing a table into smaller, more manageable parts based on a specific column or set of columns. This can help optimize query performance and reduce the amount of data processed.

Example:

```sql
CREATE TABLE employee_partitioned (
   emp_id INT,
   emp_name STRING,
   emp_salary FLOAT
)
PARTITIONED BY (dept_name STRING);

LOAD DATA INPATH '/user/hive/employee_data.csv' 
INTO TABLE employee_partitioned 
PARTITION (dept_name='Sales');
```

This creates a partitioned table called `employee_partitioned` partitioned by `dept_name`. Data is loaded into the `Sales` partition using the partition clause in the `LOAD DATA` command.

## Conclusion

Apache Hive provides a powerful SQL-based interface for querying and analyzing large datasets in Hadoop. With HiveQL's SQL-like syntax, you can easily manipulate and extract valuable insights from your data. The basic concepts and commands covered in this guide provide a solid foundation for those new to Hive development.