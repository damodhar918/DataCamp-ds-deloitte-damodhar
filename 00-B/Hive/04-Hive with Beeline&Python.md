# Connecting to Hive with Beeline Client Using Python

To connect to Hive from Python, you can use the Beeline client which provides a JDBC/ODBC connection to Hive. Here's an example of connecting to Hive with Beeline using Python:

## Prerequisites

Before we begin, you'll need to have the following installed:

- Python
- Beeline client
  - You can download the Beeline client from the [Apache Hive releases page](https://hive.apache.org/downloads.html).

## Example

Here's an example of connecting to Hive with Beeline in Python:

```python
import subprocess

def connect_to_hive():
  # start Beeline shell process
  beeline_process = subprocess.Popen(['beeline', '-u', 'jdbc:hive2://<host>:<port>/<database>;transportMode=http'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  # wait for beeline process to finish starting up
  beeline_process.wait()

  # send command to authenticate with Hive
  beeline_process.stdin.write('!connect <username> <password>\n')

  stdout, stderr = beeline_process.communicate()

  # check if connection was successful
  if '0: jdbc:hive2://' in stdout:
    print('Connected to Hive!')
    return beeline_process
  else:
    print('Connection to Hive failed!')
    return None
```

The `connect_to_hive()` function starts the Beeline shell process, waits for it to finish starting up, and then sends a command to authenticate with Hive. The function returns the Beeline process if the connection was successful, or `None` if the connection failed.

Once you have a Beeline process, you can execute queries on Hive using the `beeline_process.stdin.write()` method. For example:

```python
beeline_process = connect_to_hive()

if beeline_process is not None:
  # execute query
  beeline_process.stdin.write('SELECT * FROM my_table;\n')

  # read output
  stdout, stderr = beeline_process.communicate()

  print(stdout)
else:
  print('Connection to Hive failed!')
```

This code connects to Hive, executes a SQL query, and then prints the output to the console.

Note that the Beeline client allows you to execute multiple statements in a single session, so you can execute multiple queries without having to reconnect to Hive each time. To execute multiple queries in a single session, just separate them with a semicolon (`;`). For example:

```python
beeline_process = connect_to_hive()

if beeline_process is not None:
  # execute multiple queries
  beeline_process.stdin.write('SELECT * FROM my_table_1;\n')
  beeline_process.stdin.write('SELECT * FROM my_table_2;\n')
  beeline_process.stdin.write('SELECT * FROM my_table_3;\n')

  # read output
  stdout, stderr = beeline_process.communicate()

  print(stdout)
else:
  print('Connection to Hive failed!')
```

This code executes three SQL queries in a single session and prints the output to the console.

That's it! This is a basic example of how to connect to Hive with Beeline using Python. With this setup, you can now execute Hive queries from Python without having to use the Hive JDBC driver directly.
