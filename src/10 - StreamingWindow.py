from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
from pyspark.sql.functions import current_timestamp
from pyspark.sql.functions import window


spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

socketStreamDF = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

currentTimeDF = socketStreamDF.withColumn("processingTime", current_timestamp())

# Split the lines into words
wordsDF = currentTimeDF.select(
   explode(
       split(currentTimeDF.value, " ")
   ).alias("word"), currentTimeDF.processingTime.alias("Time"))

windowedWords = wordsDF\
    .groupBy(window(wordsDF.Time, "1 minute"), wordsDF.word)\
    .count().orderBy("window")

# Start running the query that prints the running counts to the console
query = windowedWords \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
