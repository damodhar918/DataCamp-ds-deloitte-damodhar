To install PySpark, follow these steps:

1. Download and install Java Development Kit (JDK) 8 or later.
   Download link: https://www.oracle.com/java/technologies/javase-downloads.html

2. Download and install Apache Spark with Hadoop.

   - Go to the Spark download page: https://spark.apache.org/downloads.html
   - Select the latest Spark version and choose the package type that corresponds to your operating system and Hadoop version.
   - Once you have downloaded the package, extract it to a local directory of your choice.

3. Set up the environment variables required to use PySpark. Open a terminal and enter the following commands:

   - `export SPARK_HOME=<Path_to_Spark_directory>` (replace `<Path_to_Spark_directory>` with the actual path where you extracted the Spark package).
   - `export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin`
   - `export PYSPARK_PYTHON=<Path_to_python2.7>` (replace `<Path_to_python2.7>` with the actual path where python2.7 is installed).

4. Test the installation by running the PySpark shell using the command:

   ```
   pyspark
   ```

   You should see the PySpark interactive shell prompt. To test a simple PySpark command, enter the following:

   ```
   >>> rdd = sc.parallelize([1, 2, 3, 4, 5])
   >>> rdd.take(3)
   [1, 2, 3]
   ```

   If the above command executes successfully and displays the output, then the installation is complete and PySpark is ready to use.