from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Create DataFrame representing the stream of input lines from connection to localhost:9999
# This acts like the source of data
lines = spark \
    .readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Split the lines into words
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

print(words.printSchema())

# Generate running word count
wordCounts = words.groupBy("word").count()

print(wordCounts.printSchema())

# Keep the partitions as 3
spark.conf.set("spark.sql.shuffle.partitions", "3")

# print('Before Setting -> ' + spark.conf.get("spark.sql.adaptive.enabled"))
# spark.conf.set("spark.sql.adaptive.enabled", False)
# print('Before Setting -> ' + spark.conf.get("spark.sql.adaptive.enabled"))

# Start running the query that prints the running counts to the console
# Make sure that you have chmod 777 access to the checkpoints folder
query = wordCounts \
    .writeStream \
    .option("checkpointLocation", "/Users/<YOUR_MACHINE_USER_NAME>/checkpoints") \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
