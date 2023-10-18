
import subprocess
import re


class Executor:
    def __init__(self, beeline: str, hive2: str):
        self.beeline = beeline
        self.hive2 = hive2

    def execute_subprocess(self, commands: list) -> str:
        process = subprocess.Popen(
            commands, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8')

    def execute_beeline_query(self, query: str) -> str:
        commands = [self.beeline, '-u', self.hive2, '-e', query]
        return self.execute_subprocess(commands)


class TableSchemaAnalyzer:
    def __init__(self, query_executor: Executor):
        self.query_executor = query_executor

    def get_column_data_types(self, table_name: str) -> set:
        describe_query = f"DESCRIBE EXTENDED {table_name}"
        describe_output = self.query_executor.execute_beeline_query(
            describe_query)
        type_lines = [line for line in describe_output.splitlines()
                      if 'struct' in line]
        types = set()
        for line in type_lines:
            m = re.match(r'^\s+(\w+):\w+\((\d+)\):(\w+)\s+', line)
            if m:
                types.add(m.group(3))
        return types


class SchemaTransformer:
    def __init__(self, schema: str):
        self.schema = schema

    def generate_temp_table_with_all_strings(self) -> str:
        columns = self.schema.strip().replace(
            'CREATE TABLE my_table (', '').replace(');', '').split(',')
        string_columns = [f'{col_name} STRING' for col_name in columns]
        new_schema = ', '.join(string_columns)
        return f'CREATE TEMPORARY TABLE temp_table ({new_schema});'

    def generate_cast_table_statements(self) -> str:
        columns = self.schema.strip().replace(
            'CREATE TABLE my_table (', '').replace(');', '').split(',')
        cast_columns = [f"CAST({col_name} AS {col_type}) AS {col_name}"
                        for col_name, col_type in [
                            col.split() for col in columns]]
        new_schema = ', '.join(cast_columns)
        return f'CREATE TABLE my_cast_table AS SELECT \
{new_schema} FROM temp_table;'


class SchemaTransformerManager:
    def __init__(self, schema_transformer: SchemaTransformer):
        self.schema_transformer = schema_transformer

    def transform_schema(self):
        temp_table_statement = self.schema_transformer.\
            generate_temp_table_with_all_strings()
        cast_table_statements = self.schema_transformer.\
            generate_cast_table_statements()
        print(temp_table_statement)
        print(cast_table_statements)


if __name__ == '__main__':
    beeline = 'beeline'
    hive2 = 'hivePath'
    schema = 'schema'
    table = 'table'

    query_executor = Executor(beeline,  hive2)
    table_schema_analyzer = TableSchemaAnalyzer(query_executor)
    column_data_types = table_schema_analyzer.get_column_data_types('my_table')
    print(sorted(column_data_types))

    test_file_path = 'test_file.hql'
    with open(test_file_path, 'r') as f:
        schema = ''.join(f.readlines()[1:])
    schema_transformer = SchemaTransformer(schema)
    schema_transformer_manager = SchemaTransformerManager(schema_transformer)
    schema_transformer_manager.transform_schema()
