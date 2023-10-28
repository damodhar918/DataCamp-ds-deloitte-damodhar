Connecting to a Spark cluster in PySpark is a straightforward process. Here's an example of how to do it:

```python
from pyspark import SparkContext, SparkConf

# create a Spark configuration object
conf = SparkConf().setAppName("MyApp").setMaster("local")

# create a Spark context object
sc = SparkContext(conf=conf)
```

In this example, we create a SparkConf object with some optional attributes like the application name (`"MyApp"`) and the master URL (`"local"`, which means run everything locally). Then we pass this configuration object to the constructor of a SparkContext object. Once we have a SparkContext, we can start interacting with the Spark cluster.

For example, we might use the `textFile` method of the SparkContext to read in a text file and create a RDD (Resilient Distributed Dataset):

```python
text_rdd = sc.textFile("file.txt")
```

This will create a RDD containing all the lines of the text file `file.txt`. We can then perform various transformations and actions on this RDD using PySpark's API.