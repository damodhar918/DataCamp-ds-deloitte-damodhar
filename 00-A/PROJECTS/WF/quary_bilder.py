# cat quary.py

# need to work
import os
import subprocess

# Read tables list from tables.txt file
with open("tables.txt", "r") as f:
    tables_list = f.read().splitlines()

# Read databases list from databases.txt file
with open("databases.txt", "r") as f:
    databases_list = f.read().splitlines()

# Connect to Hive using Beeline tool
beeline_cmd = "/opt/mapr/hive/hive-2.3/bin/beeline -u jdbc:hive2://edl-b02-services.uat.bigdata.wellsfargo.net:10000/default;auth=maprsasl;saslQop=auth-conf;ssl=true; -e "

# Define queries to retrieve table information
metadata_query = "DESCRIBE %s.%s;"
count_query = "SELECT COUNT(*) FROM %s.%s;"

# Retrieve table information for each table in tables list and database in databases list
for database_name in databases_list:
    for table_name in tables_list:
        # Retrieve metadata for current table and database
        process = subprocess.Popen(beeline_cmd + metadata_query %
                                   (database_name, table_name), stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        metadata_rows = output.decode().splitlines()

        # Extract columns names and number of columns
        columns_list = []
        for row in metadata_rows:
            column_name = row.split("\t")[0]
            if column_name != "":
                columns_list.append(column_name)
        num_columns = len(columns_list)

        # Retrieve number of records
        process = subprocess.Popen(beeline_cmd + count_query %
                                   (database_name, table_name), stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        num_records = int(output.decode().splitlines()[1])

        # Print table information
        print("TABLE: %s.%s" % (database_name, table_name))
        print("Number of Columns: %d" % num_columns)
        print("Number of Records: %d" % num_records)
        print("Column Names: %s" % ",".join(columns_list))
        print("=======================================")
