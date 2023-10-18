import subprocess
import re
from pyhive import hive
from pyarrow import parquet as pq
from typing import Dict, List

# Define the Hadoop paths to the DDL and Parquet files
ddl_path = '/path/to/ddl/file'
parquet_path = '/path/to/parquet/file'

# Define the name of the Hive database to use
database_name = 'my_database'

# Define a dictionary mapping DDL data types to Parquet data types
type_map = {
    'int': 'int',
    'bigint': 'bigint',
    'float': 'float',
    'double': 'double',
    'string': 'string',
    'timestamp': 'timestamp',
    'date': 'date',
    'boolean': 'boolean'
    # Add more data types as needed
}

# Define a function to parse the DDL file and extract the column names and data types
def parse_ddl(ddl_path: str) -> Dict[str, str]:
    with open(ddl_path, 'r') as f:
        ddl_text = f.read()
    ddl_lines = ddl_text.splitlines()
    table_name = None
    column_defs = {}
    for line in ddl_lines:
        if 'CREATE TABLE' in line:
            table_name = line.split()[-1].strip()
        elif table_name and '(' in line and ')' in line:
            col_def = line.split('(')[1].split(')')[0].strip()
            col_name, col_type = col_def.split()
            column_defs[col_name] = col_type
    return table_name, column_defs

# Define a function to load the Parquet file into a temporary view in the Hive database
def load_parquet_to_view(parquet_path: str, view_name: str, database_name: str) -> None:
    subprocess.run(['beeline', '-u', f'jdbc:hive2://{hive_host}:10000/{database_name}', '-n', hive_user, '-p', hive_password, '-e', f"CREATE TEMPORARY VIEW {view_name} AS SELECT * FROM parquet.`{parquet_path}`"])

# Define a function to map the data types from the DDL file to the columns in the Parquet file
def map_data_types(ddl_cols: Dict[str, str], parquet_cols: List[str]) -> Dict[str, str]:
    col_types = {}
    for col_name in parquet_cols:
        if col_name in ddl_cols:
            ddl_type = ddl_cols[col_name].lower()
            if ddl_type in type_map:
                col_types[col_name] = type_map[ddl_type]
    return col_types

# Define a function to create a new Hive table with the mapped data types and sample records
def create_table_with_mapped_types(ddl_table_name: str, parquet_view_name: str, database_name: str, col_types: Dict[str, str]) -> None:
    with hive.connect(host=hive_host, port=10000, database=database_name, auth='CUSTOM', configuration={'sasl.qop': 'auth'}) as conn:
        cursor = conn.cursor()
        create_ddl = f"CREATE TABLE {ddl_table_name} (\n"
        for col_name, col_type in col_types.items():
            create_ddl += f"{col_name} {col_type},\n"
        create_ddl = create_ddl[:-2] + "\n)"
        cursor.execute(create_ddl)
        insert_sql = f"INSERT INTO {ddl_table_name} SELECT * FROM {parquet_view_name} LIMIT 5"
        cursor.execute(insert_sql)
        conn.commit()

# Parse the DDL file and extract the column names and data types
table_name, ddl_cols = parse_ddl(ddl_path)

# Load the Parquet file into a temporary view in the Hive database
parquet_view_name = f'temp_view_{table_name}'
load_parquet_to_view(parquet_path, parquet_view_name, database_name)

# Get the column names and types from the Parquet file
parquet_file = pq.ParquetFile(parquet_path)
parquet_schema = parquet_file.schema
parquet_cols = [field.name for field in parquet_schema]

# Map the data types from the DDL file to the columns in the Parquet file
col_types = map_data_types(ddl_cols, parquet_cols)

# Check for missing or mismatched columns in the DDL file
missing_cols = set(parquet_cols) - set(ddl_cols.keys())
if missing_cols:
    print(f"WARNING: The DDL file is missing the following columns from the Parquet file: {', '.join(sorted(missing_cols))}")
mismatched_cols = set(ddl_cols.keys()) - set(parquet_cols)
if mismatched_cols:
    print(f"WARNING: The DDL file contains the following columns that are not in the Parquet file: {', '.join(sorted(mismatched_cols))}")
for col_name, col_type in col_types.items():
    if col_type is None:
        print(f"ERROR: The data type for column '{col_name}' cannot be mapped from the DDL file")
        exit(1)

# Create a new Hive table with the mapped data types and sample records
ddl_table_name = f'{table_name}_mapped'
create_table_with_mapped_types(ddl_table_name, parquet_view_name, database_name, col_types)

# Print the first five records from the new table
with hive.connect(host=hive_host, port=10000, database=database_name, auth='CUSTOM', configuration={'sasl.qop': 'auth'}) as conn:
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {ddl_table_name} LIMIT 5")
    results = cursor.fetchall()
    for row in results:
        print(row)
        
        
        
        
# ----
import os
import subprocess

# Define path to Parquet file and Beeline connection information
parquet_file = "/path/to/parquet_file.parquet"
beeline_connection = "jdbc:hive2://localhost:10000/default"

# Define DDL for new table
new_table_ddl = "CREATE EXTERNAL TABLE new_table(column1 string, column2 int)"

# Define Beeline command to create a temporary view
create_temp_view = f"beeline -u {beeline_connection} -e 'CREATE TEMPORARY VIEW temp_view AS SELECT * FROM parquet.`{parquet_file}`'"

# Define Beeline command to create new table from DDL and load data from temp view
create_new_table = "beeline -u {beeline_connection} -e 'DROP TABLE IF EXISTS new_table; {new_table_ddl}; INSERT INTO TABLE new_table SELECT * FROM temp_view;'"

# Define Beeline command to select and print 5 records from new table
print_new_table = "beeline -u {beeline_connection} -e 'SELECT * FROM new_table LIMIT 5;'"

# Execute Beeline commands
os.system(create_temp_view)
os.system(create_new_table)
os.system(print_new_table)


# ----------------
import os
import subprocess

# Define path to Parquet file and Beeline connection information
parquet_file = "/path/to/parquet_file.parquet"
beeline_connection = "jdbc:hive2://localhost:10000/default"

# Define DDL for new table
new_table_ddl = "CREATE EXTERNAL TABLE new_table(column1 string, column2 int, column3 float, column4 double, column5 decimal(10,2), column6 timestamp, column7 date, column8 boolean)"

# Define dictionary mapping temporary table/view column data types to new table column data types
mapping_dict = {"column1": "string", "column2": "int", "column3": "float", "column4": "double", "column5": "decimal(10,2)", "column6": "timestamp", "column7": "date", "column8": "boolean"}

# Define Beeline command to create a temporary view
create_temp_view = f"beeline -u {beeline_connection} -e 'CREATE TEMPORARY VIEW temp_view AS SELECT * FROM parquet.`{parquet_file}`'"

# Define Beeline command to create new table from DDL and load data from temp view with casted data types
create_new_table = "beeline -u {beeline_connection} -e 'DROP TABLE IF EXISTS new_table; {new_table_ddl}; INSERT INTO TABLE new_table SELECT "
for i, col in enumerate(mapping_dict.keys()):
    if i > 0:
        create_new_table += ", "
    if mapping_dict[col] == "string":
        create_new_table += f"CAST({col} AS STRING)"
    elif mapping_dict[col] == "int":
        create_new_table += f"CAST({col} AS INT)"
    elif mapping_dict[col] == "float":
        create_new_table += f"CAST({col} AS FLOAT)"
    elif mapping_dict[col] == "double":
        create_new_table += f"CAST({col} AS DOUBLE)"
    elif "decimal" in mapping_dict[col]:
        create_new_table += f"CAST({col} AS {mapping_dict[col]})"
    elif mapping_dict[col] == "timestamp":
        create_new_table += f"CAST({col} AS TIMESTAMP)"
    elif mapping_dict[col] == "date":
        create_new_table += f"CAST({col} AS DATE)"
    elif mapping_dict[col] == "boolean":
        create_new_table += f"CAST({col} AS BOOLEAN)"
    else:
        create_new_table += col
create_new_table += " FROM temp_view;'"

# Define Beeline command to select and print 5 records from new table
print_new_table = "beeline -u {beeline_connection} -e 'SELECT * FROM new_table LIMIT 5;'"

# Execute Beeline commands
os.system(create_temp_view)
os.system(create_new_table)
os.system(print_new_table)

# -----------
import subprocess

# Define the Hadoop paths to the DDL and Parquet files
ddl_path = '/path/to/ddl/file'

# Define the name of the Hive database and table to use
database_name = 'my_database'
table_name = 'my_table'

# Define a function to execute a query in Beeline and return the output
def execute_beeline_query(query: str, database_name: str) -> str:
    process = subprocess.Popen(['beeline', '-u', f'jdbc:hive2://{hive_host}:10000/{database_name}', '-n', hive_user, '-p', hive_password, '-e', query], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode('utf-8')

# Execute a DESCRIBE EXTENDED statement on the table and obtain the column data types
describe_query = f"DESCRIBE EXTENDED {table_name}"
describe_output = execute_beeline_query(describe_query, database_name)
type_lines = [line for line in describe_output.splitlines() if 'struct' in line]
types = set()
for line in type_lines:
    m = re.match(r'^\s+(\w+):\w+\((\d+)\):(\w+)\s+', line)
    if m:
        types.add(m.group(3))
print(sorted(types))