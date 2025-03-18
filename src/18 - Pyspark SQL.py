from pyspark.sql import SparkSession
from config.definitions import DATA_DIR
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession \
    .builder \
    .appName("Rate Source") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

file_path = f"{DATA_DIR}/people.json"

df = spark.read \
        .option("inferSchema", "True") \
        .json(file_path)

df.show()






