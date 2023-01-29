from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("TriggerExample") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Create DataFrame representing the stream of input lines from connection to localhost:9999
# This acts like the source of data
linesDF = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()


# This is like writing the data to the sink, console in this case
query = linesDF \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .trigger(processingTime='15 seconds') \
    .start()

query.awaitTermination()
