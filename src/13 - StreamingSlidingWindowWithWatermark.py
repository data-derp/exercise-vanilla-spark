from pyspark.sql.functions import *
from pyspark.sql.types import *

from config.spark import init_spark, get_socket_stream

if __name__ == "__main__":
    spark = init_spark("Sliding Window With Watermark")

    socketStreamDF = get_socket_stream(spark)

    stocksDF = socketStreamDF.withColumn("value", split("value", ","))\
         .withColumn("EventTime", to_timestamp(col("value")[0], "yyyy-MM-dd HH:mm:ss")) \
         .withColumn("symbol", col("value")[1]).withColumn("price", col("value")[2].cast(DoubleType()))

    stocksDF.printSchema()

    # Group the data by window and word and compute the count of each group
    windowedWords = stocksDF\
        .withWatermark("EventTime", "2 minute") \
        .groupBy(window("EventTime", "1 minute", "30 seconds"), stocksDF.symbol)\
        .agg(max("price").alias("MaximumPrice"))

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




