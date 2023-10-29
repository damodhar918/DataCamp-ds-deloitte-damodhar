# PySpark Developer: Installation and Configuration on Windows

In this document, we will cover the installation and configuration of PySpark on Windows operating system.

## Prerequisites:

- Java 1.8 with JDK 8 is required for the installation. You can download it from [here](https://www.oracle.com/in/java/technologies/downloads/#java8-windows) after logging in to Oracle website.

  - Download the executable file from the above-mentioned link.
  - Install it in the directory `C:\Program Files\Java\jdk1.8.0_201` (default directory).
  - Set the environment variable `JAVA_HOME` to the installation directory i.e., `C:\Program Files\Java\jdk1.8.0_201`.
  - Append the path `%JAVA_HOME%\bin` to the system path variable.

- Apache Spark is the main tool for PySpark programming and it can be downloaded from [here](https://spark.apache.org/downloads.html).

  - Choose the appropriate version and download the package.
  - Unzip the package to `C:\spark` directory (default location).
  - Set the environment variable `SPARK_HOME` to the installation directory i.e., `C:\spark`.
  - Set the environment variable `HADOOP_HOME` to the installation directory i.e., `C:\hadoop`.
  - Append the path `%SPARK_HOME%\bin` to the system path variable.

- For Hadoop, download `winutils.exe` file from [here](https://github.com/steveloughran/winutils/tree/master/hadoop-3.0.0/bin) and place it in `C:\spark\bin` directory.

  - Add `%HADOOP_HOME%\bin` to the system path variable.

- Python 3 is required for PySpark installation. You can download it from [here](https://www.python.org/downloads/).
  - Make sure to select and install the option for adding Python to the system path.
  - Add `C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python310\Scripts` and `C:\Users\YOUR_USER\AppData\Local\Programs\Python\Python310\` to the system path variable.

## PySpark Installation:

1. Open Command Prompt with administrator privilege.

2. Install PySpark using `pip` command. Execute the following command in the Command Prompt:

   ```
   pip install pyspark
   ```

   This will install the latest version of PySpark.

3. After the installation, set the environment variable `PYSPARK_PYTHON` to `python`.

   ```
   setx PYSPARK_PYTHON python
   ```

4. PySpark is now successfully installed and ready to use.

## PySpark Configuration:

1. Open any text editor and create a new Python file.

2. Import PySpark and create a `SparkContext` object.

   ```
   from pyspark import SparkContext
   sc = SparkContext("local", "PySpark Example")
   ```

   This will create a new local Spark Context, which can be used to interact with Spark.

3. Now, create a sample RDD and perform some operations on it to test the configuration.

   ```
   rdd = sc.parallelize([('foo', 1), ('bar', 2), ('baz', 3)])
   result = rdd.map(lambda x: (x[0], x[1] + 1)).collect()
   print(result)
   ```

   The output will be:

   ```
   [('foo', 2), ('bar', 3), ('baz', 4)]
   ```

   This means that PySpark is successfully configured and working.

### Conclusion

This document provides a detailed guide for the installation and configuration of PySpark on Windows operating system. Once installed, PySpark can be used to interact with Apache Spark and perform complex data analytics tasks.
