# Hive Date and Timestamp Functions

This guide provides a quick review of Hive Date and Timestamp functions for Hive developers. It covers the following topics:

1. Hive Date and Timestamp Functions List
2. Examples of Hive Date and Timestamp Functions
3. Extracting Year, Quarter, Month, Day from Hive Date and Timestamp
4. Extracting Hour, Minute, and Second from Hive Timestamp
5. Date Difference, Adding, and Subtracting Dates
6. Converting Date and Timestamp into String Format

## 1. Hive Date and Timestamp Functions List

The following Hive Date and Timestamp functions are used to manipulate Date and Time on HiveQL queries over Hive CLI, Beeline, and other applications:

- `from_unixtime(bigint unixtime[, string format])`
- `unix_timestamp()`
- `to_date(string timestamp)`
- `year(string date)`
- `quarter(date/timestamp/string)`
- `month(string date)`
- `day(string date)`
- `dayofmonth(date)`
- `hour(string date)`
- `minute(string date)`
- `second(string date)`
- `weekofyear(string date)`
- `extract(field FROM source)`
- `datediff(string enddate, string startdate)`
- `date_add(date startdate, tinyint/smallint/int days)`
- `date_sub(date startdate, tinyint/smallint/int days)`
- `from_utc_timestamp({any primitive type} ts, string timezone)`
- `to_utc_timestamp({any primitive type} ts, string timezone)`
- `current_date()`
- `current_timestamp()`
- `add_months(string start_date, int num_months, output_date_format)`
- `last_day(string date)`
- `next_day(string start_date, string day_of_week)`
- `trunc(string date, string format)`
- `months_between(date1, date2)`
- `date_format(date/timestamp/string ts, string fmt)`

## 2. Examples of Hive Date and Timestamp Functions

The following are examples of Hive Date and Timestamp functions:

- `from_unixtime(1605108612)` returns `2020-11-11 15:30:12`
- `unix_timestamp('2020-11-11 15:30:12.084')` returns `1605108612`
- `to_date('2020-11-11 15:30:12.084')` returns `2020-11-11`
- `current_date()` returns `2020-11-11`
- `current_timestamp()` returns `2020-11-11 15:27:05.741`
- `from_utc_timestamp(1605108612,'PST')` returns `1970-01-19 05:51:48.612`
- `to_utc_timestamp(1605108612,'PST')` returns `1970-01-19 21:51:48.612`
- `year('2020-11-11')` returns `2020`
- `quarter('2020-11-11')` returns `4`
- `month('2020-02-28')` returns `2`
- `day('2020-02-28')` returns `28`
- `dayofmonth('2020-02-28')` returns `28`
- `hour('2020-11-11 15:30:12.084')` returns `15`
- `minute('2020-11-11 15:30:12.084')` returns `30`
- `second('2020-11-11 15:30:12.084')` returns `12`
- `extract(month from '2020-11-20')` returns `11`
- `datediff('2020-11-01','2020-11-11')` returns `-11`
- `date_add('2020-11-11',2)` returns `2020-11-13`
- `date_sub('2020-11-11',2)` returns `2020-11-09`
- `add_months('2020-11-11',2)` returns `2021-01-11`
- `last_day('2020-11-11')` returns `2020-11-30`
- `next_day('2020-02-11','FRI')` returns `2020-02-14`
- `trunc('2020-02-11','YYYY')` returns `2020-01-01`
- `months_between('2020-11-11','2020-02-11')` returns `9.0`
- `date_format('2020-11-09','dd-MM-YYYY')` returns `09-11-2020`

## 3. Extracting Year, Quarter, Month, Day from Hive Date and Timestamp

Use the following functions to extract year, quarter, month, and day from hive date and timestamp:

- `year(string date)`
- `quarter(date/timestamp/string)`
- `month(string date)`
- `day(string date)`
- `dayofmonth(date)`

## 4. Extracting Hour, Minute, and Second from Hive Timestamp

Use the following functions to extract hour, minute, and second from hive timestamp:

- `hour(string date)`
- `minute(string date)`
- `second(string date)`
- `extract(field FROM source)`

## 5. Date Difference, Adding, and Subtracting Dates

Use the following functions to calculate the difference between dates, add days, and subtract days:

- `datediff(string enddate, string startdate)`
- `date_add(date startdate, tinyint/smallint/int days)`
- `date_sub(date startdate, tinyint/smallint/int days)`

## 6. Converting Date and Timestamp into String Format

Use the following function to convert date and timestamp into string format:

- `date_format(date/timestamp/string ts, string fmt)`


### Additional Examples
Sure, here are examples for every function in the Hive Date and Timestamp functions list:

1. `from_unixtime(bigint unixtime[, string format])`

Example: 
```
SELECT from_unixtime(1605108612);
-- Returns: 2020-11-11 15:30:12
```

2. `unix_timestamp()`

Example:
```
SELECT unix_timestamp('2020-11-11 15:30:12.084');
-- Returns: 1605108612
```

3. `to_date(string timestamp)`

Example:
```
SELECT to_date('2020-11-11 15:30:12.084');
-- Returns: 2020-11-11
```

4. `year(string date)`

Example:
```
SELECT year('2020-11-11');
-- Returns: 2020
```

5. `quarter(date/timestamp/string)`

Example:
```
SELECT quarter('2020-11-11');
-- Returns: 4
```

6. `month(string date)`

Example:
```
SELECT month('2020-02-28');
-- Returns: 2
```

7. `day(string date)`

Example:
```
SELECT day('2020-02-28');
-- Returns: 28
```

8. `dayofmonth(date)`

Example:
```
SELECT dayofmonth('2020-02-28');
-- Returns: 28
```

9. `hour(string date)`

Example:
```
SELECT hour('2020-11-11 15:30:12.084');
-- Returns: 15
```

10. `minute(string date)`

Example:
```
SELECT minute('2020-11-11 15:30:12.084');
-- Returns: 30
```

11. `second(string date)`

Example:
```
SELECT second('2020-11-11 15:30:12.084');
-- Returns: 12
```

12. `weekofyear(string date)`

Example:
```
SELECT weekofyear('2020-11-11');
-- Returns: 46
```

13. `extract(field FROM source)`

Example:
```
SELECT extract(month from '2020-11-20');
-- Returns: 11
```

14. `datediff(string enddate, string startdate)`

Example:
```
SELECT datediff('2020-11-01','2020-11-11');
-- Returns: -11
```

15. `date_add(date startdate, tinyint/smallint/int days)`

Example:
```
SELECT date_add('2020-11-11', 2);
-- Returns: 2020-11-13
```

16. `date_sub(date startdate, tinyint/smallint/int days)`

Example:
```
SELECT date_sub('2020-11-11', 2);
-- Returns: 2020-11-09
```

17. `from_utc_timestamp({any primitive type} ts, string timezone)`

Example:
```
SELECT from_utc_timestamp(1605108612,'PST');
-- Returns: 1970-01-19 05:51:48.612
```

18. `to_utc_timestamp({any primitive type} ts, string timezone)`

Example:
```
SELECT to_utc_timestamp(1605108612,'PST');
-- Returns: 1970-01-19 21:51:48.612
```

19. `current_date()`

Example:
```
SELECT current_date();
-- Returns: 2020-11-11
```

20. `current_timestamp()`

Example:
```
SELECT current_timestamp();
-- Returns: 2020-11-11 15:27:05.741
```

21. `add_months(string start_date, int num_months, output_date_format)`

Example:
```
SELECT add_months('2020-11-11',2);
-- Returns: 2021-01-11
```

22. `last_day(string date)`

Example:
```
SELECT last_day('2020-11-11');
-- Returns: 2020-11-30
```

23. `next_day(string start_date, string day_of_week)`

Example:
```
SELECT next_day('2020-02-11','FRI');
-- Returns: 2020-02-14
```

24. `trunc(string date, string format)`

Example:
```
SELECT trunc('2020-02-11','YYYY');
-- Returns: 2020-01-01
```

25. `months_between(date1, date2)`

Example:
```
SELECT months_between('2020-11-11','2020-02-11');
-- Returns: 9.0
```

26. `date_format(date/timestamp/string ts, string fmt)`

Example:
```
SELECT date_format('2020-11-09','dd-MM-YYYY');
-- Returns: 09-11-2020
```