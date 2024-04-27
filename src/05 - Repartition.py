from pyspark.sql import SparkSession

from config.definitions import DATA_DIR, OUTPUT_DIR
from config.spark import init_spark
from lib.logger import Log4j

if __name__ == "__main__":
    spark = init_spark("Repartition Example")

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
    #
    input("Press Enter")

    spark.stop()
    logger.info("Finished - Repartition Example ")

