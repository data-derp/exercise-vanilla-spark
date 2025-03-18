from pyspark.sql import SparkSession
from config.definitions import DATA_DIR
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
    .builder \
    .appName("Rate Source") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

file_path1 = f"{DATA_DIR}/file/"

schema = StructType([
  StructField("greeting", StringType(), True),
])

df = (spark.readStream
      .option("header", "True")
      .format("csv")
      .option("path", file_path1)
      .schema(schema)
        .load())

# print(df.printSchema())

query = df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
