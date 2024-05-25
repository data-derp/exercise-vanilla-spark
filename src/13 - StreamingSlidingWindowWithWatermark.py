from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession \
    .builder \
    .appName("Tumbling Window Wordcount") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

socketStreamDF = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

stocksDF = socketStreamDF.withColumn("value", split("value", ","))\
     .withColumn("EventTime", to_timestamp(col("value")[0], "yyyy-MM-dd HH:mm:ss")) \
     .withColumn("symbol", col("value")[1]).withColumn("price", col("value")[2].cast(DoubleType()))

stocksDF.printSchema()

# Group the data by window and word and compute the count of each group
windowedWords = stocksDF\
    .withWatermark("EventTime", "2 minute") \
    .groupBy(window("EventTime", "1 minute", "30 seconds"), stocksDF.symbol)\
    .agg(max("price").alias("maxPrice"))

windowedWords.printSchema()

# outputDF = windowedWords.select("window.start", "window.end", "Symbol", "TotalPrice")

# outputDF.printSchema()

# This is like writing the data to the sink, console in this case
query = windowedWords \
    .writeStream \
    .outputMode("update") \
    .format("console") \
    .option('truncate', 'false') \
    .start()

query.awaitTermination()




