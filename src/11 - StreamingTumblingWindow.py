from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

from config.spark import init_spark, get_socket_stream

if __name__ == "__main__":
    spark = init_spark("Tumbling Window")

    socketStreamDF = get_socket_stream(spark)

    stocksDF = socketStreamDF.withColumn("value", split("value", ","))\
         .withColumn("EventTime", to_timestamp(col("value")[0], "yyyy-MM-dd HH:mm:ss")) \
         .withColumn("symbol", col("value")[1]).withColumn("price", col("value")[2].cast(DoubleType()))

    stocksDF.printSchema()

    # Group the data by window and word and compute the count of each group
    windowedWords = stocksDF\
        .groupBy(window("EventTime", "1 minute"), stocksDF.symbol)\
        .agg(sum("price").alias("totalPrice"))

    windowedWords.printSchema()

    # This is like writing the data to the sink, console in this case
    query = windowedWords \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .option('truncate', 'false') \
        .start()

query.awaitTermination()




