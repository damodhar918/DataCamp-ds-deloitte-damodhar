# Spark History Server to Monitor Applications

## Introduction

The Spark History Server is a User Interface that is used to monitor the metrics and performance of the completed Spark applications. In this article, we will discuss what Spark History Server is, how to enable it to collect event logs, starting the server, and finally, how to access and navigate the Interface.

## What is Spark History Server?

When you submit a Spark application, Spark context is created which ideally gives you Spark Web UI to monitor the execution of the application. However, when your application is done with the processing, Spark context will be terminated so your Web UI as well. If you wanted to see the monitoring for an already finished application, you cannot do it.

This is where Spark History Server comes into the picture, where it keeps the history (event logs) of all completed applications and its runtime information which allows you to review metrics and monitor the application later in time.

## History Server Configurations

In order to store event logs for all submitted applications, first, Spark needs to collect the information while applications are running. By default, the spark doesn’t collect event log information. You can enable this by setting the below configs on spark-defaults.conf

```
// Enable to store the event log
spark.eventLog.enabled true

// Location where to store event log
spark.eventLog.dir file:/C:/tmp/spark-events

// Location from where history server to read event log
spark.history.fs.logDirectory file:/C:/tmp/spark-events
or
spark.history.fs.logDirectory file:/C:/tmp/spark-events
```

Spark keeps a history of every application you run by creating a sub-directory for each application and logs the events specific to the application in this directory.

## Spark Start History Server

Now, start history server on Linux or mac by running.

```
$SPARK_HOME/sbin/start-history-server.sh
```

If you are running Spark on windows, you can start the history server by starting the below command.

```
$SPARK_HOME/bin/spark-class.cmd org.apache.spark.deploy.history.HistoryServer
```

## Monitor the Spark Application

By default, History server listens at 18080 port and you can access it from browser using http://localhost:18080/

By clicking on each App ID, you will get the Spark application job, stage, task, executor’s environment details.

## Spark Stop History Server

You can stop the history server by running the below command.

```
$SPARK_HOME/sbin/stop-history-server.sh
```

## Conclusion

Using the History server, you can keep track of all completed applications, you need to enable this in order to keep the history. These metrics come in handy when you are doing performance tuning.

Happy Learning !!
