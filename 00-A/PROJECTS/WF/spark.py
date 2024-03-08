> vi csv_to_hive_loader.py
from pyspark.sql import SparkSession
import sys
from pyspark.sql.types import StringType,DecimalType,DoubleType
from pyspark.sql import functions as F
 
#Inirtializing the Spark Session and setting properties as required
#spark = SparkSession.builder.appName("Insert_Query_Execution").master("yarn").enableHiveSupport().config("hive.exec.dynamic.partition","true").config("hive.exec.dynamic.partition.mode","nonstrict").config("spark.dynamicAllocation.executorIdleTimeout","10s").getOrCreate()
spark = SparkSession.builder.appName("Insert_Query_Execution").master("local").enableHiveSupport().config("hive.exec.dynamic.partition","true").config("hive.exec.dynamic.partition.mode","nonstrict").config("spark.dynamicAllocation.executorIdleTimeout","10s").getOrCreate()
spark.sql("set spark.sql.orc.impl=hive")
spark.sql("set spark.sql.orc.enableVectorizedReader=true")
spark.sql("set spark.sql.orc.enabled=true")
spark.sql("set spark.sql.hive.convertMetastoreOrc=true")
spark.sql("set spark.sql.orc.filterPushdown=true")
 
 
#Extracting Sys Arguments
partition_col_name=sys.argv[1]
partition_col_value=sys.argv[2]
target_database_name=sys.argv[3]
target_table_name=sys.argv[4]
csv_file_path=sys.argv[5]
 
 
#Reading csv data
df1=spark.read.csv(csv_file_path)
 
#Adding partition column to existing columns
df2=df1.withColumn(partition_col_name,F.lit(partition_col_value))
 
#df2.show(2,False)
 
#Creating Temp Tablre and Inserting data to Target Table
df2.registerTempTable("target_table_temp")
spark.sql("USE "+target_database_name)
spark.sql("INSERT INTO TABLE "+target_table_name+" PARTITION("+partition_col_name+") select * from target_table_temp")
 
#Stopping the Session
spark.stop()
 
 
 