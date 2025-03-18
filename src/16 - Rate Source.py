from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Rate Source") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

df = spark.readStream.format("rate").load()

# print(df.printSchema())

query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()