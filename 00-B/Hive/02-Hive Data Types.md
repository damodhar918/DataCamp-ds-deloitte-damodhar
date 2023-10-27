# Hive Data Types

This guide provides an overview of data types supported in Hive. Hive allows a wide range of data types, including numeric types, date/time types, string types, miscellaneous types, and complex types.

## Numeric Types

Hive supports various numeric types, including:

- TINYINT: 1-byte signed integer, from -128 to 127
- SMALLINT: 2-byte signed integer, from -32,768 to 32,767
- INT/INTEGER: 4-byte signed integer, from -2,147,483,648 to 2,147,483,647
- BIGINT: 8-byte signed integer, from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
- FLOAT: 4-byte single precision floating point number
- DOUBLE: 8-byte double precision floating point number
- DOUBLE PRECISION: alias for DOUBLE, only available starting with Hive 2.2.0
- DECIMAL: introduced in Hive 0.11.0 with a precision of 38 digits; user-definable precision and scale available in Hive 0.13.0; NUMERIC is the same as DECIMAL starting with Hive 3.0.0

## Date/Time Types

Hive supports various date/time types, including:

- TIMESTAMP: only available starting with Hive 0.8.0
- DATE: only available starting with Hive 0.12.0
- INTERVAL: only available starting with Hive 1.2.0

## String Types

Hive supports various string types, including:

- STRING
- VARCHAR: only available starting with Hive 0.12.0
- CHAR: only available starting with Hive 0.13.0

## Misc Types

Hive supports various miscellaneous types, including:

- BOOLEAN
- BINARY: only available starting with Hive 0.8.0

## Complex Types

Hive supports various complex types, including:

- arrays: ARRAY<data_type> (negative values and non-constant expressions allowed as of Hive 0.14)
- maps: MAP<primitive_type, data_type> (negative values and non-constant expressions allowed as of Hive 0.14)
- structs: STRUCT<col_name : data_type [COMMENT col_comment], ...>
- union: UNIONTYPE<data_type, data_type, ...> (only available starting with Hive 0.7.0)

## Column Types

Hive supports integral types (TINYINT, SMALLINT, INT/INTEGER, BIGINT) and string types. Integral literals are assumed to be INT by default, unless the number exceeds the range of INT.

## Decimal Types

The DECIMAL type in Hive is based on Java's BigDecimal. It is used for representing immutable arbitrary precision decimal numbers in Java. Hive 0.11 and 0.12 have the precision of the DECIMAL type fixed and limited to 38 digits. Hive 0.13 introduced user-definable precision and scale, and NUMERIC is the same as DECIMAL starting with Hive 3.0.0. Decimal literals provide precise values and greater range for floating-point numbers than the DOUBLE type.

## Union Types

Although UNIONTYPE was introduced in Hive 0.7.0, full support for this type in Hive remains incomplete. UNIONTYPEs are effectively pass-through-only.

## Literals

Floating point literals are assumed to be DOUBLE. Decimal literals provide precise values and greater range for floating-point numbers than the DOUBLE type.

## Casting Dates and Times

Dates and times can be cast to other data types as necessary. For example:

```
-- Cast '14:21:21' to a TIMESTAMP
SELECT CAST('14:21:21' AS TIMESTAMP);

-- Cast '14:21:21' to a DATE (note that this will use the current date as the date component)
SELECT CAST('14:21:21' AS DATE);
```

The output for the first query, which casts '14:21:21' to a TIMESTAMP, would be:

```
2021-10-03 14:21:21
```

The output for the second query, which casts '14:21:21' to a DATE (using the current date as the date component), would be:

```
2021-10-03
```

Note that the result for the first query includes both the date and time components, while the result for the second query only includes the date component.

This concludes the overview of Hive data types. For additional information, please see the Type System in the Tutorial.

## Handling of NULL Values

Missing values are represented by the special value NULL. To import data with NULL fields, check documentation of the SerDe used by the table.

This concludes the overview of Hive data types. For additional information, please see the Type System in the Tutorial.

## Examples of data types supported by Hive

### Numeric Types

- TINYINT: -64, 0, 127
- SMALLINT: -32768, 0, 32767
- INT/INTEGER: -2147483648, 0, 2147483647
- BIGINT: -9223372036854775808, 0, 9223372036854775807
- FLOAT: 1.0, 2.5, -0.25
- DOUBLE: 3.14159, 2.71828
- DECIMAL: 12345678901234567890123456789012345678, -0.12345678901234567890123456789012345678

### Date/Time Types

- TIMESTAMP: '2021-09-28 12:34:56'
- DATE: '2021-09-28'
- INTERVAL: INTERVAL '1' DAY, INTERVAL '2' YEAR TO MONTH, INTERVAL '1 2:3:4.000005' DAY

### String Types

- STRING: 'Hello, World!', 'Hive is awesome!'
- VARCHAR: 'Hello', 'Hive'
- CHAR: 'Hi!', 'Bye!'

### Misc Types

- BOOLEAN: true, false
- BINARY: 0x0A, 0x0B, 0x0C

### Complex Types

- arrays: ARRAY<int>(1, 2, 3), ARRAY<string>('Hive', 'is', 'awesome')
- maps: MAP<string, int>('one'->1, 'two'->2, 'three'->3)
- structs: STRUCT<name: string, age: int>('John', 30)
- union: UNIONTYPE<int, double, array<string>, struct<a:int,b:string>>(0:1, 1:2.0, 2:["three","four"], 3:{"a":5,"b":"five"})

Note that these are just examples, and there are many other possible values for each data type.
