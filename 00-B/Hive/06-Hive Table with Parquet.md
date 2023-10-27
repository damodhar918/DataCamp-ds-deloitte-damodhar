## Creating a Hive Table with Partition Columns

## Table Definition

Let's create a Hive table named `mytable` with partition columns `year`, `month`, and `day`. The table contains various data types including string, integer, double, and boolean.

```sql
CREATE TABLE mytable (
    id INT,
    name STRING,
    age INT,
    salary DOUBLE,
    is_employed BOOLEAN
) 
PARTITIONED BY (year INT, month INT, day INT)
ROW FORMAT DELIMITED 
FIELDS TERMINATED BY ','
STORED AS PARQUET;
```

## Loading Data

Assuming we have a parquet file named `mydata.parquet` containing the data in the following format:

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
To create and load data to a table with snappy parquet file format in Hive, you can follow the below steps:

1. Create a Parquet table with snappy compression:

   ```
   CREATE TABLE sample_table (
     id INT,
     name STRING,
     age INT
   )
   STORED AS PARQUET
   TBLPROPERTIES ('parquet.compression'='SNAPPY');
   ```

2. Load data into the table:

   ```
   LOAD DATA LOCAL INPATH '/path/to/data/sample_data.txt' INTO TABLE sample_table;
   ```

   Note: Make sure that the file path mentioned in the command is correct and the data is in the same format as the table columns.

3. Verify the data has been loaded into the table:

   ```
   SELECT * FROM sample_table;
   ```

   This command will fetch all the data from the table. You can also use various filters and aggregation functions in the SELECT statement as per your requirement.

4. Export data from table to snappy compressed parquet file:

   ```
   INSERT OVERWRITE DIRECTORY '/path/to/output/data'
   STORED AS PARQUET
   TBLPROPERTIES ('parquet.compression'='SNAPPY')
   SELECT * FROM sample_table;
   ```

   This command will export the data from the table into a snappy compressed parquet file.

Note: You can change the path of the input and output files as per your requirement. Also, make sure that the version of Hive you are using is compatible with the snappy compression library.