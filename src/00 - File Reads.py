import sys
from pyspark.sql import *
from lib.logger import Log4j
from lib.utils import *
from config.definitions import DATA_DIR

if __name__ == "__main__":
    conf = get_spark_app_config()

    spark = SparkSession.builder \
        .appName("Spark File Reads") \
        .getOrCreate()

    logger = Log4j(spark)

    logger.info("Starting Spark File Read")

    file_path1 = f"{DATA_DIR}/ratings.csv"

    # # should show you only 1 job
    ratings_df = spark.read.csv(file_path1)
    ratings_df.show()

    input("Please ENTER")

    logger.info("Finished Spark File Read")
    spark.stop()
