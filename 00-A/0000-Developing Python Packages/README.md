# impyrial

A package for converting between imperial unit lengths and weights.

This package was created for the [DataCamp](https://www.datacamp.com) course "Developing Python Packages".
[impyrial](./workspace/mypackages/impyrial/)

### Features

- Convert lengths between miles, yards, feet and inches.
- Convert weights between hundredweight, stone, pounds and ounces.

### Usage

```
import impyrial

# Convert 500 miles to feet
impyrial.length.convert_unit(500, from_unit='yd', to_unit='ft')  # returns 1500.0

# Convert 100 ounces to pounds
impyrial.weight.convert_unit(100, from_unit='oz', to_unit='lb')  # returns 6.25
```
