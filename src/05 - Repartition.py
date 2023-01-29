from pyspark.sql import *

from pyspark.sql.types import *
from lib.logger import Log4j
from pyspark.sql.functions import year, month, dayofmonth
from pyspark.sql import SparkSession
from datetime import date, timedelta
from pyspark.sql.types import IntegerType, DateType, StringType, StructType, StructField
from config.definitions import DATA_DIR,OUTPUT_DIR

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("PySpark Repartition Example") \
        .getOrCreate()

    logger = Log4j(spark)

    logger.info("STARTED - Repartition Example ")

    # Paths
    temp_df = spark.read.format("csv").\
        option("header", "true"). \
        option("inferSchema", "true").\
        load(f'{DATA_DIR}/country_data.csv')

    # let's do a simple repartition
    # temp_df.repartition(6).write.mode('overwrite').csv(f'{OUTPUT_DIR}/repartition')

    temp_df.repartition("country")\
        .write.mode('overwrite').csv(f'{OUTPUT_DIR}/repartition')

    input("Press Enter")

    spark.stop()
    logger.info("Finished - Repartition Example ")

