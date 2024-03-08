# cat beeline_sdgp_ingestion.py
####################################################################################################################################################
####################################################################################################################################################
# Script Name      : beeline_sdgp_ingestion.py (Synthetic Data Generater + )
# Script Details   : This is a script that generates mock data.
#
# usage            : beeline_sdgp_ingestion.py [-h] [-c {m,e,g}] volume {csv,parquet} csv_file [conf_csv_file]
#
#   This is a script that generates mock data.
#          1. beeline_sdgp_ingestion.py -c m 50000 csv mock_table conf.csv # Generate 50000 rows of mock data and save as mock_table_50000.csv
#          2. beeline_sdgp_ingestion.py -c e 100000 parquet edit_table.csv conf.csv # Along with given data can edit with conf.csv, generate 100000 recrds and save as edit_table_100000.parquet
#          3. beeline_sdgp_ingestion.py -c g 1000000 csv scale.csv # Generate 1000000  # rows of mock data by scaling existing data and save as scale_1000000.csv
# positional arguments:
#   volume                The size. An integer value that specifies how many rows to generate mock data. Recommended
#                         minimum value is more than volume size or more than 1000.
#   {csv,parquet}         The type of format to save the mock data. csv for CSV format, parquet for Parquet format.
#   csv_file              The CSV file name. A string value that specifies the name of the CSV file to read or write.
#   conf_csv_file         The configuration CSV file name. A string value that specifies the name of the configuration
#                         CSV file to read. This argument is required if mode is e or g.
# options:
#   -h, --help            show this help message and exit
#   -c {m,e,g}, --choice {m,e,g}
#                         The type of function to select. m for mock data, e for edit mock data, g for generate high
#                         volume data.
#
# ================================================================================================================================================
#    Date of Change                         Developer                                                                   Change Log
# ==================================================================================================================================================
#     2023-09-06                            Damodhar Jangam (damodhar.jangam@ccc.com)                            Initial Creation
####################################################################################################################################################


import pandas as pd
import numpy as np
import hashlib
import random
import time
import datetime
from datetime import datetime, timedelta
import argparse
import pyarrow as pa
import pyarrow.parquet as pq
from pathlib import Path
import sys
from colorama import Fore, Back, Style
import os
import exrex
import dask.dataframe as dd
from dask import delayed
import subprocess
import json


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

    def __init__(self, volume: int, file: str, conf_file: str, format: str, choice: str):
        """
        Constructor for the DataGenerator class.
        Args:
            volume (int): The number of rows to generate for the mock data.
            file (str): The name of the CSV file to generate / sameple file to edit and generate.
            conf_file (str): The name of the configuration CSV file to read.
            format (str): The format to save the mock data (either "csv" or "parquet").
            choice (str): The type of function to select ("m" for mock data, "e" for edit mock data, "g" for generate high volume data).
        """
        self.n = int(volume * 1.0)  # Number of rows to generate
        self.volume = volume  # Number of rows to volume
        self.file = file.strip().split('.')[0]  # File name to generate
        self.csv_file_path = f"{self.file}.csv"  # to read CSV file path
        self.start_time = time.time()
        try:
            with open(format.strip()) as f:
                self.properties = json.load(f)
                print(self.properties)
        except Exception as e:
            print(f"Pass valid json file {format} !", e, sep='\n')
        self.choice = choice
        if conf_file:
            self.conf_file_path = f"{conf_file.split('.')[0]}.csv"
            self.conf_df = self.checkFile(self.conf_file_path).astype(str)
            self.conf_dict = self.conf_df.to_dict(
                orient='index')  # Configuration dictionary

    @property
    def clock(self):
        return f"; Time taken: {time.strftime('%X', time.gmtime(time.time() - self.start_time))}"

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
            df = pd.read_csv(path).rename(columns=lambda x: x.split(".")[-1])
            print(f"Fetched the file {path}!", self.clock.strip(" ;"))
            return df
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

    def ingest(self):
        """
        Save a DataFrame in CSV format.

        Args:
            df (pd.DataFrame): DataFrame to save.
        """

        df = self.df_mock.sample(self.volume).drop_duplicates()
        partition_columns = self.properties['partition_columns']
        partition_columns = [x.lower() for x in partition_columns]
        hive1 = self.properties['hive1']
        schema = self.properties['schema']
        table = self.properties['table']
        beeline = self.properties['beeline']
        COLUMNS_TO_INGEST = [*df.columns]
        [COLUMNS_TO_INGEST.remove(x) for x in partition_columns]
        # self.mock_file_csv_path = f"{self.file}_{self.choice}_{self.volume}.csv"
        # df.to_csv(self.mock_file_csv_path, index=False, header=True)
        insert_statements = []
        if partition_columns:
            for i, j in df.groupby(partition_columns):
                j = j.reset_index(drop=True).drop(
                    partition_columns, axis=1)[COLUMNS_TO_INGEST]
                partition = " partition ( "+', '.join([f'{key}="{value}"' for key, value in zip(
                    partition_columns, i)]) + " )" if partition_columns else ""
                query = "insert into "+schema+"."+table + partition+" {} values  {}".format(
                    "( "
                    + ", ".join(([*j.columns]))
                    + " )",
                    ", ".join(
                        (
                            "( "
                            + ", ".join('"{}"'.format(row.iloc[i])
                                        for i in range(len(j.columns)))
                            + " )"
                        )
                        for _, row in j.iterrows()
                    )
                )+";"
                insert_statements.append(query)
        else:
            query = "insert into "+schema+"."+table + " {} values  {}".format(
                    "( "
                    + ", ".join(([*df.columns]))
                    + " )",
                    ", ".join(
                        (
                            "( "
                            + ", ".join('"{}"'.format(row.iloc[i])
                                        for i in range(len(df.columns)))
                            + " )"
                        )
                        for _, row in df.iterrows()
                    )
            )+";"
            insert_statements.append(query)
        load_cmd = [
            beeline,
            "-u",
            hive1,
            "-e",
            ''.join(insert_statements),]
        subprocess.run(load_cmd)
        print(f"ingestinted {df.shape[0]} records !",
              self.clock.strip(" ;"), load_cmd)

    def genMockData(self, df) -> pd.DataFrame:
        """
        Create a mock DataFrame by randomly selecting values from the original DataFrame.

        Args:
            df (pd.DataFrame): Original DataFrame.

        Returns:
            pd.DataFrame: Mock DataFrame.
        """
        self.columns = df.columns
        # self.df_mock = pd.DataFrame(columns=self.columns)
        # for i in range(len(self.columns)):
        #     self.df_mock[self.columns[i]] = np.random.choice(
        #         df[self.columns[i]].unique(), self.n)
        self.df_mock = pd.concat(

            [df.apply(lambda a: a.sample(frac=1).values)
             for _ in range(int(self.n/df.shape[0]))],
            ignore_index=True,
        )

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
        return [(item.get('name').strip().lower(), item.get('values').strip()) for item in self.conf_dict.values() if item.get('type').strip() == type]

    def addRandomDuration(self, start_date, so, eo, format):
        random_duration = pd.to_timedelta(random.uniform(pd.to_timedelta(
            so).total_seconds(), pd.to_timedelta(eo).total_seconds()), unit='s')
        return (start_date + random_duration).strftime(format)

    def genrateUniqueIndexs(self, start):
        start = int(start)
        return np.arange(start, start + self.n)

    def generateDependentDateRanges(self, data):
        preDate, so, eo, format = self.splitByPipe(data)
        return pd.to_datetime(self.df_mock[preDate])\
            .apply(lambda x: self.addRandomDuration(x, so, eo, format))

    def generateComposites(self, data):
        keys = self.splitByPipe(data)
        return self.df_mock[keys].astype('str').sum(1).apply(lambda x: hashlib.sha1(x.encode()).hexdigest())

    def generateWithConf(self, unique=False) -> pd.DataFrame:
        """
        Generates mock data for different types of configuration items and assigns them to columns in the mock DataFrame.

        Returns:
            pd.DataFrame: The mock DataFrame with generated data.
        """
        if unique:
            df = pd.DataFrame()
            for column, start_number in self.uniqueIndexs:
                start_number = int(start_number)
                self.df_mock[column] = np.arange(
                    start_number, start_number + self.n)
                # print(delayed(self.genrateUniqueIndexs)(start_number))
                # df[column] = delayed(self.genrateUniqueIndexs)(column,start_number)

            for column, data in self.dependentDateRanges:
                preDate, so, eo, format = self.splitByPipe(data)
                self.df_mock[column] = pd.to_datetime(self.df_mock[preDate])\
                    .apply(lambda x: self.addRandomDuration(x, so, eo, format))
                # df[column] = delayed(self.generateDependentDateRanges)(data)

            for column, data in self.composites:
                keys = self.splitByPipe(data)
                self.df_mock[column] = self.df_mock[keys].astype('str').sum(1).apply(
                    lambda x: hashlib.sha1(x.encode()).hexdigest())
                # df[column] = delayed(self.generateComposites)(data)
            # df = dd.from_delayed(df.values.tolist(),meta=df)
            # print(df.head())
            # exit()
            return self.df_mock

        self.uniqueIndexs = self.getByType("uniqueIndex")
        self.dateRanges = self.getByType("dateRange")
        self.dates = self.getByType("date")
        self.categories = self.getByType("category")
        self.constants = self.getByType("constant")
        self.floatRanges = self.getByType("floatRange")
        self.intRanges = self.getByType("intRange")
        self.constants = self.getByType("constant")
        self.times = self.getByType("time")
        self.dependentDateRanges = self.getByType("dependentDateRange")
        self.composites = self.getByType("composite")
        self.regexPatterns = self.getByType("regexPattern")

        for column, start_number in self.uniqueIndexs:
            start_number = int(start_number)
            self.df_mock[column] = np.arange(
                start_number, start_number + self.n)

        for column, date in self.dates:
            date, format = self.splitByPipe(date)
            self.df_mock[column] = pd.to_datetime(date).strftime(format)

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
            s, e, format = self.splitByPipe(data)
            random_dates = [datetime.now() + timedelta(hours=random.randint(0, 24),
                                                       minutes=random.randint(0, 60), seconds=random.randint(0, 60)) for _ in range(self.n)]
            self.df_mock[column] = [pd.to_datetime(
                date).strftime(format) for date in random_dates]

        for column, data in self.dateRanges:
            s, e, format = self.splitByPipe(data)
            self.df_mock[column] = self.generateDates(s, e, format)

        for column, data in self.dependentDateRanges:
            preDate, so, eo, format = self.splitByPipe(data)
            self.df_mock[column] = pd.to_datetime(self.df_mock[preDate]).apply(
                lambda x: self.addRandomDuration(x, so, eo, format))

        for column, data in self.regexPatterns:
            self.df_mock[column] = self.df_mock.iloc[:, 0].apply(
                lambda x: exrex.getone(data))

        for column, data in self.composites:
            keys = self.splitByPipe(data)
            self.df_mock[column] = self.df_mock[keys].astype('str').sum(1).apply(
                lambda x: hashlib.sha1(x.encode()).hexdigest())

        return self.df_mock

    # def output(self):
    #     """
    #     Checks the output format and calls the corresponding method to save the generated data.
    #     """

    #     if self.outputFormat == "csv":
    #         self.saveInCSV()
    #     elif self.outputFormat == "parquet":
    #         self.saveInParquet()

    def generateMockData(self):
        """
        Generates mock data based on the given configuration and saves it.
        """
        self.df_mock = pd.DataFrame()
        if self.volume > 10000:
            self.n = 11000
            self.df_mock = self.generateWithConf()
            self.n = int(self.volume*1.1)
            print(f"Generateing !", self.clock.strip(" ;"))
            self.genMockData(self.df_mock)
            print(f"Generateing !", self.clock.strip(" ;"))
            self.generateWithConf(unique=True)
            print(f"Generateing !", self.clock.strip(" ;"))
        else:
            self.df_mock = self.generateWithConf()
        self.ingest()

    def editMockDataAndGenerate(self):
        """
        Reads a CSV file, generates mock data based on the existing data, edit and saves it.
        """
        df = self.checkFile(self.csv_file_path)
        self.genMockData(df)
        self.generateWithConf()
        self.ingest()

    def justScaleData(self):
        """
        Reads a CSV file, generates mock data based on the existing data, and saves it.
        """
        df = self.checkFile(self.csv_file_path)
        self.genMockData(df)
        self.ingest()


if __name__ == '__main__':
    # Create a parser object with a description of your script
    parser = argparse.ArgumentParser(
        description="""This is a script that generates mock data.\n
\t1. beeline_sdgp_ingestion.py -c m 50000 csv mock_table conf.csv # Generate 50000 rows of mock data and save as mock_table_50000.csv\n
\t2. beeline_sdgp_ingestion.py -c e 100000 parquet edit_table.csv conf.csv # Along with given data can edit with conf.csv, generate 100000 recrds and save as edit_table_100000.parquet\n
\t3. beeline_sdgp_ingestion.py -c g 1000000 csv scale.csv # Generate 1000000 rows of mock data by scaling existing data and save as scale_1000000.csv\n
""")

    # Add arguments to the parser object
    parser.add_argument("-c", "--choice", type=str, choices=[
                        'm', 'e', 'g'], help="The type of function to select. m for mock data, e for edit mock data, g for generate high volume data.")
    # Add a volume argument to the parser object
    parser.add_argument(
        "volume", type=int, help="The size. An integer value that specifies how many rows to generate mock data. Recommended minimum value is more than volume size or more than 1000.")
    parser.add_argument(
        "format", type=str, help="The type of format to save the mock data. csv for CSV format, parquet for Parquet format.")

    parser.add_argument("csv_file", type=str,
                        help="The CSV file name. A string value that specifies the name of the CSV file to read or write.")
    # Change this line to make conf_csv_file optional for some modes
    parser.add_argument("conf_csv_file", type=str, default=None, nargs='?',
                        help="The configuration CSV file name. A string value that specifies the name of the configuration CSV file to read. This argument is required if mode is e or g.")

    # Parse the arguments
    args = parser.parse_args()
    # Change the mode variable to choice
    choice = args.choice
    LENGTH = 122
    print(Fore.CYAN + '#'*LENGTH+Fore.WHITE)
    # Pass the arguments to your class constructor as parameters
    data_gen = DataGenerator(volume=args.volume, file=args.csv_file.strip('.\\'),
                             conf_file=args.conf_csv_file.strip('.\\'),  format=args.format, choice=choice)

    def suggestion():
        print(Fore.CYAN + '#'*LENGTH+Fore.WHITE)
        print(Fore.CYAN + '#'+Fore.WHITE, end='')
        print(
            " If you have any suggestion or any question, please contact Damodhar Jangam (damodhar.jangam@wellsfargo.com).           ",
            "Or leave your comments in https://confluence.wellsfargo.net/display/CAP/Synthetic+Data+Generator+%28SDG%29+Plus        ",
            "You can access latest code in https://github.wellsfargo.com/K078158/Synthetic-data-generator-plus                      ",
            sep=Fore.CYAN + "#\n# " + Fore.WHITE,
            end='')

        print(Fore.CYAN + '#'+Fore.WHITE,)
        print(Fore.CYAN + '#'*LENGTH+Fore.WHITE)
    # Use the choice argument to select a function from your class
    if choice == 'm' and args.conf_csv_file:

        data_gen.generateMockData()

        suggestion()
    elif choice == 'e' and args.conf_csv_file:
        data_gen.editMockDataAndGenerate()
        suggestion()
    elif choice == 'g':
        data_gen.justScaleData()
        suggestion()

    else:
        print(" Invalid choice or configuration file not found!\n try: beeline_sdgp_ingestion.py -h for help")
        print(Fore.CYAN + '#'*LENGTH+Fore.WHITE)
