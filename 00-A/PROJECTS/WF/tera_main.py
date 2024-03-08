import pyarrow.parquet as pq
import pyarrow as pa
import time
import traceback
from teradataml import *
import random
from datetime import datetime, timedelta
import datetime
import numpy as np
import pandas as pd
main.py
####################################################################################################################################################
# Script Name      : main.py (Teradata Data Ingestion with Synthetic Data)
# Script Details   : This script for work with Teradata Vantage
#
# usage: main.py [-h] ddl_path [csv_file] number_records schema_name table_name if_exists [{m,e,g}] [conf_csv_file]
# This is a script that generates mock data and ingests it into Teradata.
#       1) python main.py ddl.txt vc_cdb_cust_email_sample.csv 8000000 d_cap_curated vc_cdb_cust_email1 replace
#       2) python main.py ddl.txt _ 1000000 d_cap_curated vc_cdb_cust_email1 replace m vc_cdb_cust_email_conf.csv
#       2) python main.py ddl.txt vc_cdb_cust_email_sample.csv 8000000 d_cap_curated vc_cdb_cust_email1 replace e vc_cdb_cust_email_conf.csv
# Teradata Data Ingestion with Syntathetic Data
#
# positional arguments:
#   ddl_path        Input ddl info (only columns and datatypes) at the end primary key if any
#   csv_file        input sample CSV file path.  Skip if mode is 'e' or 'g'.
#   number_records  Number of records to ingest into teradata
#   schema_name     Target teradata schema name
#   table_name      Target table name
#   if_exists       Specifies the action to take when table already exists in Vantage. Valid values: 'fail', 'replace', 'append'
#                   mostly prefer 'replace'
#   {m,e,g}         The type of function to select. m for mock data, e for edit mock data, g for generate high volume data.
#                   Default is g.
#   conf_csv_file   The configuration CSV file name. A string value that specifies the name of the configuration CSV file to
#                   read. This argument is required if mode is e or g.
#
# options:
#   -h, --help      show this help message and exit
#
# ================================================================================================================================================
#    Date of Change                         Developer                                                                   Change Log
# ==================================================================================================================================================
#     2023-07-14                            Damodhar Jangam (damodhar.jangam@wellsfargo.com)                            Initial Creation
#     2023-09-14                            Damodhar Jangam (damodhar.jangam@wellsfargo.com)                            integrated with SDGP scripts
####################################################################################################################################################


class DataGenerator:
    """
    The 'DataGenerator' class is used to generate and manipulate data based on given configurations. It has methods to convert a date string into a pandas datetime object, generate random dates within a given range, save a DataFrame in CSV and Parquet file formats, create a mock DataFrame by randomly selecting values from the original DataFrame, retrieve configuration items by type, split a string by pipe character, generate mock data for different types of configuration items, and edit the mock data. The class also has placeholder methods for generating high volume data and editing the mock data.
    Args:
            volume (int): The number of rows to generate for the mock data.
            file (str): The name of the CSV file to generate / sameple file to edit and generate.
            conf_file (str): The name of the configuration CSV file to read.
            format (str): The format to save the mock data (either "csv" or "parquet").
            choice (str): The type of function to select ("m" for mock data, "e" for edit mock data, "g" for generate high volume data).
    """

    def __init__(self, volume: int, file: str, conf_file: str, format: str = 'csv', choice: str = 'g'):
        """
        Constructor for the DataGenerator class.
        Args:
            volume (int): The number of rows to generate for the mock data.
            file (str): The name of the CSV file to generate / sameple file to edit and generate.
            conf_file (str): The name of the configuration CSV file to read.
            format (str): The format to save the mock data (either "csv" or "parquet").
            choice (str): The type of function to select ("m" for mock data, "e" for edit mock data, "g" for generate high volume data).
        """
        self.n = int(volume * 1.1)  # Number of rows to generate
        self.volume = volume  # Number of rows to volume
        self.file = file.split('.csv')[0]  # File name to generate
        self.csv_file_path = f"{self.file}.csv"  # to read CSV file path
        self.outputFormat = format
        self.choice = choice

        if conf_file:
            self.conf_file_path = f"{conf_file.strip('.csv')}.csv"
            self.conf_df = self.checkFile(self.conf_file_path)
            self.conf_dict = self.conf_df.to_dict(
                orient='index')  # Configuration dictionary

    def checkDate(self, date):
        """
        Convert a date string into a pandas datetime object.
        Args:
            date (str): A string representing a date in the format "YYYY-MM-DD".
        Returns:
            pd.Timestamp: A pandas datetime object representing the input date.
        Example Usage:
            date = "2022-01-01"
            result = check_date(date)
            print(result)
        Code Analysis:
            The method tries to convert the input date string into a pandas datetime object using the pd.to_datetime function.
            If the conversion is successful, the method returns the datetime object.
            If an exception occurs during the conversion, the method prints the error message and continues execution.
        """
        try:
            return pd.to_datetime(date)
        except Exception as e:
            print(e)
            pass

    def checkFile(self, path) -> pd.DataFrame:
        try:
            return pd.read_csv(path).rename(columns=lambda x: x.split(".")[-1])
        except Exception as e:
            sys.exit(f'{e}')

    def generateDates(self, s, e, format) -> list:
        """
        Generate random dates within a given range.
        Args:
            s (str): Start date in the format "YYYY-MM-DD".
            e (str): End date in the format "YYYY-MM-DD".
        Returns:
            list: List of datetime objects representing the generated dates.
        """
        start = self.checkDate(s)
        end = self.checkDate(e)
        if start > end:
            raise ValueError(
                "Start date must be before end date. (start date < end date)")
        dates = []
        for i in range(self.n):
            date = start + (end - start) * random.random()
            dates.append(date.strftime(str(format)))
        return dates

    def saveInCSV(self):
        """
        Save a DataFrame in CSV format.
        Args:
            df (pd.DataFrame): DataFrame to save.
            file_name (str): File name for the CSV file.
        """
        df = self.df_mock.sample(self.volume).drop_duplicates()
        self.mock_file_csv_file = f"{self.file}_{self.choice}_{self.volume}.csv"
        df.to_csv(self.mock_file_csv_file, index=False, header=True)
        print(f"CSV file has been saved as { self.mock_file_csv_file}!")

    # def saveInParquet(self):
    #     """
    #     Save a DataFrame in Parquet format.
    #     Args:
    #         df (pd.DataFrame): DataFrame to save.
    #         file_name (str): File name for the Parquet file.
    #     """
    #     df = self.df_mock.sample(self.volume).drop_duplicates()
    #     self.mock_file_csv_file = f"{self.file}_{self.choice}_{self.volume}.parquet"
    #     table = pa.Table.from_pandas(df, preserve_index=False)
    #     pq.write_table(table,  self.mock_file_csv_file, compression="snappy")
    #     print(f"Parquet file has been saved as { self.mock_file_csv_file}!")

    def genMockData(self, df) -> pd.DataFrame:
        """
        Create a mock DataFrame by randomly selecting values from the original DataFrame.
        Args:
            df (pd.DataFrame): Original DataFrame.
        Returns:
            pd.DataFrame: Mock DataFrame.
        """
        self.columns = df.columns.str.upper()
        self.df_mock = pd.DataFrame(columns=self.columns)
        for i in range(len(self.columns)):
            self.df_mock[self.columns[i]] = np.random.choice(
                df[self.columns[i]].unique(), self.n)
        return self.df_mock

    def splitByPipe(self, data):
        """
        Splits a string by pipe character and returns a list of strings.
        Args:
            data (str): The string to split.
        Returns:
            list: A list of strings after splitting by pipe character.
        """
        return [*map(str.strip, data.split("|"))]

    def getByType(self, type) -> list:
        """
        Retrieves the name and values of configuration items that match a given type from the configuration dictionary.
        Args:
            type (str): The type of configuration items to retrieve.
        Returns:
            list: A list of tuples, where each tuple contains the 'name' and 'values' of a configuration item that matches the given type.
        """
        return [(item.get('name').strip().upper(), item.get('values').strip()) for item in self.conf_dict.values() if item.get('type').strip() == type]

    def generateWithConf(self) -> pd.DataFrame:
        """
        Generates mock data for different types of configuration items and assigns them to columns in the mock DataFrame.
        Returns:
            pd.DataFrame: The mock DataFrame with generated data.
        """

        self.uniqueIndexs = self.getByType("uniqueIndex")
        self.dateRanges = self.getByType("dateRange")
        self.dates = self.getByType("date")
        self.categories = self.getByType("category")
        self.constants = self.getByType("constant")
        self.floatRanges = self.getByType("floatRange")
        self.intRanges = self.getByType("intRange")
        self.constants = self.getByType("constant")
        self.times = self.getByType("time")

        for column, start_number in self.uniqueIndexs:
            start_number = int(start_number)
            self.df_mock[column] = np.arange(
                start_number, start_number + self.n)

        for column, data in self.dateRanges:
            s, e, format = self.splitByPipe(data)
            self.df_mock[column] = self.generateDates(s, e, format)

        for column, date in self.dates:
            date, format = self.splitByPipe(date)
            self.df_mock[column] = pd.to_datetime(date).strftime(str(format))

        for column, data in self.categories:
            suffle_data = self.splitByPipe(data)
            self.df_mock[column] = np.random.choice(suffle_data, self.n)

        for column, data in self.floatRanges:
            s, e, l = [*map(float, self.splitByPipe(data))]
            self.df_mock[column] = np.round(
                np.random.uniform(s, e, self.n), int(l))

        for column, data in self.intRanges:
            s, e = [*map(int, self.splitByPipe(data))]
            self.df_mock[column] = np.random.randint(s, e, self.n)

        for column, data in self.constants:
            self.df_mock[column] = data

        for column, data in self.times:
            random_dates = [datetime.now() + timedelta(hours=random.randint(0, 24),
                                                       minutes=random.randint(0, 60), seconds=random.randint(0, 60)) for _ in range(self.n)]
            self.df_mock[column] = [pd.to_datetime(date).strftime(
                "%H:%M:%S") for date in random_dates]

        return self.df_mock

    def output(self):
        """
        Checks the output format and calls the corresponding method to save the generated data.
        """
        if self.outputFormat == "csv":
            self.saveInCSV()
        # elif self.outputFormat == "parquet":
        #     self.saveInParquet()

    def generateMockData(self):
        """
        Generates mock data based on the given configuration and saves it.
        """
        self.df_mock = pd.DataFrame()
        return self.generateWithConf().sample(self.volume).drop_duplicates()

    def editMockDataAndGenerate(self):
        """
        Reads a CSV file, generates mock data based on the existing data, edit and saves it.
        """
        df = self.checkFile(self.csv_file_path)
        self.genMockData(df)
        return self.generateWithConf().sample(self.volume).drop_duplicates()

    def justScaleData(self):
        """
        Reads a CSV file, generates mock data based on the existing data, and saves it.
        """
        df = self.checkFile(self.csv_file_path)
        return self.genMockData(df).sample(self.volume).drop_duplicates()


class TeradataDataIngestion(DataGenerator):
    """Class to deals with
        __init__: Initializes the class with the host, username and password.
        schema_table: Defines the schema and table name.
        teradata_info: Returns information about the Teradata table.
        teradata_df: Returns the Teradata table as a DataFrame of 5 records.
        teradata_count: Returns the number_records of rows in the Teradata table.
        create_connection: Establishes a connection to Teradata.
        read_csv: Reads an input CSV file.   
        exception_line: Prints error message and line number_records where exception occurred.
        create_replace_table: Replaces or creates a table with defined data types.
        fast_load: Ingests DataFrame to Teradata Vantage using Fastload.
        suffle_df_along_field: Returns shuffled DataFrame along the column. 
    """

    def __init__(self, host: str, username: str, password: str, dg: DataGenerator) -> None:
        self.HOST = host
        self.USERNAME = username
        self.PASSWORD = password
        self.start_time = time.time()
        if dg.choice in ['g', 'e']:
            self.df = dg.checkFile(dg.csv_file_path)

    @property
    def clock(self):
        return f"; Time taken: {time.strftime('%X', time.gmtime(time.time() - self.start_time))}"

    def schema_table(self, schema_name: str, table_name: str) -> None:
        """ Define table properties

        Args:
            schema_name (str): Schema Name
            table_name (str): Table Name
        """
        self.schema_name = schema_name
        self.table_name = table_name

    @property
    def teradata_info(self):
        return DataFrame(in_schema(schema_name=self.schema_name, table_name=self.table_name)).info()

    @property
    def teradata_df(self):
        return DataFrame(in_schema(schema_name=self.schema_name, table_name=self.table_name))

    @property
    def teradata_count(self):
        return (DataFrame(in_schema(schema_name=self.schema_name, table_name=self.table_name))).shape[0]

    def create_connection(self) -> None:
        """To Establish connection
        """
        self.con_tera = create_context(
            host=self.HOST, username=self.USERNAME, password=self.PASSWORD)
        print(f"Connected : {self.con_tera}", self.clock)

    def read_csv(self, path: str, delimiter: str = None) -> None:
        """Read input CSV file

        Args:
            path (str): input path
            delimiter (str, optional): delimiter type. Defaults to None.
        """

        self.path = path
        self.df = pd.read_csv(self.path,
                              dtype=self.dtypes,
                              delimiter=delimiter)
        # self.df.columns = self.df.columns.str.lower()
        self.no_input_recods = (self.df).shape[0]
        print('Fetch data:', self.no_input_recods, self.clock)

    def read_bulk_csv(self, path: str, dtypes: dict = None) -> None:
        """Read input CSV file

        Args:
            path (str): input path
            dtypes (dict): DataFrame data types. Defaults to None.
            delimiter (str, optional): delimiter type. Defaults to None.
        """
        self.bulk_csv_file = path
        self.bulk_csv_dtypes = dtypes
        self.bulk_csv_df = pd.read_csv(self.path, dtype=dtypes)
        self.bulk_csv_no_input_recods = (self.bulk_csv_df).shape[0]
        print('Fetch data:', self.bulk_csv_no_input_recods, self.clock)

    def bulk_csv_fast_load(self):
        if self.bulk_csv_no_input_recods >= 100000:
            n = int(self.bulk_csv_no_input_recods /
                    1000000) if int(self.bulk_csv_no_input_recods/1000000) == 0 else 1
            df_split = np.array_split(self.bulk_csv_df, n)
            for df_n in (df_split):
                self.fast_load(df_n)
        else:
            self.copy_to_sql(self.bulk_csv_df)

    def exception_line(self, e):
        print('Error:', e)
        tb = traceback.extract_tb(e.__traceback__)
        line_number_records = tb[-1][1]
        print(f"Exception occurred on line {line_number_records}")

    def create_replace_table(self) -> None:
        """Replace or create table

        """
        try:
            def_df = self.df[0:0]
            copy_to_sql(df=def_df,
                        table_name=self.table_name,
                        schema_name=self.schema_name,
                        temporary=False,
                        if_exists='replace',
                        primary_index=self.primary_index,
                        types=self.types
                        )
            print("Table:", self.table_name,
                  "has been created in", self.schema_name, self.clock)
        except Exception as e:
            self.exception_line(e)

    def scale_df(self, no: int) -> pd.DataFrame:
        return pd.concat(
            [self.df.apply(lambda a: a.sample(frac=1).values)
             for _ in range(int(no/self.df.shape[0]))],
            ignore_index=True,
        )

    def fast_load(self, df, if_exists: str) -> None:
        """DataFrame to Teradata Vantage using Fastload.
        Args:
            df (DataFrame)
        """
        try:
            fastload(df=df,
                     table_name=self.table_name,
                     schema_name=self.schema_name,
                     if_exists=if_exists,
                     primary_index=self.primary_index,
                     types=self.types
                     )
            # print('No. of records Ingested', len(df))
        except Exception as e:
            self.exception_line(e)
            self.copy_to_sql(df, if_exists=if_exists)

    @property
    def suffle_df_along_field(self):
        """Returning the shuffled DataFrame 
        along the column
        Returns:
            DataFrame
        """
        return self.df.apply(lambda a: a.sample(frac=1).values)

    def bulk_fast_load(self, no: int, no_dfs: int, if_exists: str) -> None:
        """ ingest DataFrame which has greater
        than 100,000 to have better performance.
        Args:
            no (int): No. records to ingest
            no_dfs (int): multiply df
        """
        x = int(no/(self.no_input_recods*no_dfs))
        if x == 0:
            self.copy_to_sql(pd.concat([self.suffle_df_along_field for _ in range(
                int(no/self.df.shape[0]))]), if_exists=if_exists)
        else:
            for i in range(x):
                self.copy_to_sql(
                    pd.concat(
                        [self.suffle_df_along_field for _ in range(int(no_dfs))]),
                    if_exists=if_exists)
                print('No. of records Ingested:', int(
                    self.no_input_recods*no_dfs*(i+1)), self.clock)

    def copy_to_sql(self, df: DataFrame, if_exists: str) -> None:
        """DataFrame to Teradata Vantage.
        with records < 100000
        Args:
            df (DataFrame)
        """
        try:
            copy_to_sql(df=df,
                        table_name=self.table_name,
                        schema_name=self.schema_name,
                        if_exists=if_exists,
                        primary_index=self.primary_index,
                        types=self.types)

        except Exception as e:
            self.exception_line(e)

    def read_ddl_types(self, ddl: str) -> None:
        """Read DDL and primary key
        Args:
            ddl (str): DDL
        """
        with open(ddl) as file:
            ddl = file.read()

        # Creating the types dictionary
        str_dict = {}
        for line in ddl.split('\n'):
            if line.strip(', '):
                parts = line.strip().split(' ')
                str_dict[parts[0].strip(' ').upper()] = parts[1].strip(
                    ', ').upper()
        try:
            self.primary_index = str_dict.pop('PRIMARY_INDEX', None)
        except KeyError:
            self.primary_index = str_dict.pop('primary_index', None)
        except:
            self.primary_index = None
            print('primary_index not found in DDL. Skipping')
        # Mapping dictionary
        teradata_type_mapping = {
            "INTEGER": INTEGER,
            "CHAR": CHAR,
            "DATE": DATE,
            "TIMESTAMP": TIMESTAMP,
            "DECIMAL": DECIMAL,
            "VARCHAR": VARCHAR,
            "TIME": TIME,
            "BINARY": BYTEINT,
        }
        pandas_type_mapping = {
            "INTEGER": "int64",
            "CHAR": "object",
            "DATE": "datetime64",
            "TIMESTAMP": "datetime64",
            "DECIMAL": "float64",
            "VARCHAR": "object",
            "TIME": "datetime64",
            "BINARY": "object",
        }

        # Convert string data types to pandas data types
        self.dtypes = {key: pandas_type_mapping.get(value.split(
            "(")[0], "object") for key, value in str_dict.items()}
        # Convert string data types to Teradata data types
        self.types = {key: teradata_type_mapping.get(value.split("(")[0], "VARCHAR")(*map(int, value.split("(")[1][:-1].split(
            ','))) if "(" in value else teradata_type_mapping.get(value.split("(")[0], "VARCHAR") for key, value in str_dict.items()}


# -----------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    import json
    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(description="""Teradata Data Ingestion with Syntathetic Data
                                    1. python main.py ddl.txt vc_cdb_cust_email_sample.csv 8000000 d_cap_curated vc_cdb_cust_email1 replace
                                    2. python main.py ddl.txt _ 1000000 d_cap_curated vc_cdb_cust_email1 replace m vc_cdb_cust_email_conf.csv
                                    3. python main.py ddl.txt vc_cdb_cust_email_sample.csv 8000000 d_cap_curated vc_cdb_cust_email1 replace e vc_cdb_cust_email_conf.csv
                                     """)

    # Add the arguments
    parser.add_argument(
        'ddl_path', type=str, help='Input ddl info (only columns and datatypes) at the end primary key if any')
    parser.add_argument('csv_file', type=str, default=None, nargs='?',
                        help='input sample CSV file path. pass _ if using mock data')
    parser.add_argument('number_records', type=int,
                        help='Number of records to ingest into teradata')
    parser.add_argument('schema_name', type=str,
                        help='Target teradata schema name')
    parser.add_argument('table_name', type=str, help='Target table name')
    parser.add_argument('if_exists', type=str,
                        help="Specifies the action to take when table already exists in Vantage. Valid values: 'fail', 'replace', 'append' mostly prefer 'replace'")
    parser.add_argument("choice", type=str, choices=['m', 'e', 'g'], default='g', nargs='?',
                        help="The type of function to select. m for mock data, e for edit mock data, g for generate high volume data. Default is g.")
    parser.add_argument("conf_csv_file", type=str, default=None, nargs='?',
                        help="The configuration CSV file name. A string value that specifies the name of the configuration CSV file to read. This argument is required if mode is e or g.")

    # Parse the arguments
    args = parser.parse_args()
    # Now you can use the arguments as variables in your code
    schema_name = args.schema_name
    table_name = args.table_name
    ddl_path = args.ddl_path.strip(' .\\')
    csv_file = args.csv_file.strip(' .\\')
    number_records = args.number_records
    if_exists = args.if_exists
    choice = args.choice
    conf_csv_file = args.conf_csv_file.strip(
        ' .\\') if args.conf_csv_file else None
    data_gen = DataGenerator(volume=number_records, file=csv_file,
                             conf_file=conf_csv_file,  format=None, choice=choice)

    # Use the choice argument to select a function from your class
    if choice == 'm' and args.conf_csv_file:
        df = data_gen.generateMockData()
    elif choice == 'e' and args.conf_csv_file:
        df = data_gen.editMockDataAndGenerate()
    elif choice == 'g':
        df = data_gen.justScaleData()
    # Get Teradata credentials
    try:
        with open("configuration.json") as f:
            config = json.load(f)
    except:
        config = {
            "HOST": "XXXX.wellsfargo.com",
            "USERNAME": "tXXXXX",
            "PASSWORD": "DatXXXXXXXXXX_dev"
        }

    tdi = TeradataDataIngestion(host=config["HOST"],
                                username=config["USERNAME"],
                                password=config["PASSWORD"], dg=data_gen)
    tdi.read_ddl_types(ddl=ddl_path)
    # Create Connection
    tdi.create_connection()
    # Define table
    tdi.schema_table(schema_name=schema_name,
                     table_name=table_name)
    print(df.shape[0], 'records are ready to ingest!', tdi.clock.strip(' ;'))
    # Ingest data to table
    tdi.copy_to_sql(df, if_exists)
    print("Teradata Data Ingestion Completed!")
    print('Info:', tdi.table_name,
          tdi.schema_name,
          tdi.teradata_count,
          tdi.clock.strip(" ;"),
          sep="\n- ")
