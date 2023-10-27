# CAST...FORMAT with SQL:2016 datetime formats

The `CAST` function in Hive allows you to convert data type from one to another. With the addition of SQL:2016 datetime formats, it is now possible to cast datetime values to strings and strings to datetime values with a specified format.

## Usage

The syntax for the `CAST` function with SQL:2016 datetime format is as follows:

- `CAST(<timestamp/date> AS <varchar/char/string> [FORMAT <template>])`
- `CAST(<varchar/char/string> AS <timestamp/date> [FORMAT <template>])`

The `FORMAT` keyword is used to specify the pattern/template for the datetime value or string.

## Example

The following are examples of using the `CAST` function with SQL:2016 datetime format:

- To cast a `timestamp` value to a `string` with the format `DD-MM-YYYY`:

  ```sql
  SELECT CAST(dt AS STRING FORMAT 'DD-MM-YYYY') FROM table_name;
  ```

- To cast a `string` value to a `date` with the format `DD-MM-YYYY`:

  ```sql
  SELECT CAST('01-05-2017' AS DATE FORMAT 'DD-MM-YYYY') FROM table_name;
  ```

## Template Elements (Tokens)

SQL:2016 datetime formats has a list of tokens that can be used to form datetime templates, including:

- Numeric temporal tokens
- Character temporals
- Timezone tokens
- Separators
- ISO 8601 delimiters
- Nested strings (text)
- Format modifier tokens

For each token, there are notes and specifications on how it can be used in the datetime template, and its conflicts and limitations with other tokens.

## Conclusion

With SQL:2016 datetime formats, Hive developers now have more flexibility and control over converting datetime values to and from strings with custom formats. Familiarizing yourself with the tokens and templates will help you take full advantage of this feature.