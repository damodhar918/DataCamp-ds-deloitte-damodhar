## Creating a Hive Table with Partition Columns

## Table Definition

Let us now create a Hive table named `mytable` which consists of partition columns, namely, `year`, `month`, and `day`. Additionally, the table incorporates a variety of data types, including string, integer, double, and boolean.

```sql
CREATE TABLE mytable (
    id INTEGER,
    name STRING,
    age INTEGER,
    salary DOUBLE,
    is_employed BOOLEAN
)
PARTITIONED BY (year INTEGER, month INTEGER, day INTEGER)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS PARQUET;
```

## Loading Data

Suppose that we have a parquet file named `mydata.parquet` that contains data in the following format:

```csv
123,John,25,35000.0,true,2021,11,24
456,Jane,30,55000.0,false,2021,11,23
789,Mark,40,75000.0,true,2021,11,22
```

We can load this data into the `mytable` Hive table using the following command:

```sql
INSERT INTO TABLE mytable PARTITION (year=2021, month=11, day)
SELECT id, name, age, salary, is_employed, day
FROM (
  SELECT *, CASE WHEN day = 24 THEN '24' WHEN day = 23 THEN '23' ELSE '22' END AS day
  FROM parquet.`mydata.parquet`
) AS t;
```

This command reads the data from the parquet file and adds a computed `day` column to match the partition column format. It then inserts the data into the `mytable` Hive table with the partition columns set to `year=2021`, `month=11`, and `day` from the computed column. 

Now you can easily query the data using partition column filters like:

```
SELECT * FROM mytable WHERE year=2021 AND month=11 AND day='24';
``` 

This will return only the rows with partition values `year=2021`, `month=11`, and `day=24`.

### Snappy Compression Parquet File Format
To create and load data to a table with snappy parquet file format in Hive, you can follow the steps mentioned below:

1. Create a Parquet table with snappy compression:

   ```
   CREATE TABLE sample_table (
     id INTEGER,
     name STRING,
     age INTEGER
   )
   STORED AS PARQUET
   TBLPROPERTIES ('parquet.compression'='SNAPPY');
   ```

2. Load data into the table:

   ```
   LOAD DATA LOCAL INPATH '/path/to/data/sample_data.txt' INTO TABLE sample_table;
   ```

   Note: Ensure that the file path mentioned in the command is precise and the data is in the same format as the table columns.

3. Verify if the data has been loaded into the table:

   ```
   SELECT * FROM sample_table;
   ```

   This command will fetch all the data from the table. You can also employ various filters and aggregation functions in the SELECT statement as per your requirement.

4. Exporting data from table to a snappy compressed parquet file:

   ```
   INSERT OVERWRITE DIRECTORY '/path/to/output/data'
   STORED AS PARQUET
   TBLPROPERTIES ('parquet.compression'='SNAPPY')
   SELECT * FROM sample_table;
   ```

   This command will export the data from the table into a snappy compressed parquet file.

Note: You can modify the path of the input and output files depending on your requirement. Additionally, ensure that the version of Hive you are using supports the snappy compression library.

Suppose you are using HiveQL; in that case, you can use the IF clause to check for empty values and substitute them with null while loading the data from the CSV file to the table.

For example, if you have a table named 'mytable' with columns named 'column1', 'column2', and 'column3', you can load data from a CSV file named 'data.csv' and substitute empty values with null using the following command:

```
LOAD DATA INPATH 'hdfs:///path/to/data.csv'
INTO TABLE mytable
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
(column1, column2, column3)
SET column1 = IF(column1 = '', NULL, column1),
    column2 = IF(column2 = '', NULL, column2),
    column3 = IF(column3 = '', NULL, column3);
```

This command will load the data from the CSV file into the 'mytable' table, where the 'column1', 'column2', and 'column3' columns will contain null values if their corresponding values in the CSV file are empty.