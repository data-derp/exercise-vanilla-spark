from pyspark.sql import *

from pyspark.sql.types import *

from config.spark import init_spark
from lib.logger import Log4j
# from lib.utils import *
from pyspark.sql.functions import year, month, dayofmonth
from pyspark.sql import SparkSession
from datetime import date, timedelta
from pyspark.sql.types import IntegerType, DateType, StringType, StructType, StructField
from config.definitions import DATA_DIR, OUTPUT_DIR

if __name__ == "__main__":
    spark = init_spark("PySpark Shuffle Partitions")

    logger = Log4j(spark)

    logger.info("STARTED Shuffle Partitions")

    # File path
    file_path = f"{DATA_DIR}/TemperaturesByCountry.csv"

    # read data
    df = spark.read.option("header", "true")\
        .option("inferSchema", "true")\
        .csv(file_path)

    # A few interesting things to check
    # x = df.groupBy(df.Country).count()
    # # x.show()
    # # spark.range(1, 10).count()
    # print(type(x))
    # print(x)

    # Let's group by and write the data back
    # df.groupBy(df.Country)\
    #     .count()\
    #     .write \
    #     .mode('overwrite') \
    #     .csv(f'{OUTPUT_DIR}/shuffle-partitions')

    # # # # check the partitions, you will get 200
    print(spark.conf.get('spark.sql.shuffle.partitions'))
    # # # # #
    # # # # # Now lets set up the shuffle partitions as 5
    spark.conf.set('spark.sql.shuffle.partitions', '5')
    # # # # # # # #
    # # # # # # # # # The same job will have 5 shuffle partitions now
    # # # # # # #
    df.groupBy(df.Country) \
        .count() \
        .write \
        .mode('overwrite') \
        .csv(f'{OUTPUT_DIR}/shuffle-partitions')

    # # # check the partitions, you will get 5
    print(spark.conf.get('spark.sql.shuffle.partitions'))

    # # # # Exercise 3.1
    # # # data = [1, 2, 3, 4, 5]
    # # # # Create data into a distributed data structure (RDD)
    # # # distData = spark.sparkContext.parallelize(data, 6)
    # # # # let's print the type of the distributed data structure
    # # # print(distData.collect())
    # # #
    # # Hold the output to see the Spark UI
    input("Press Enter")

    # # logger.info("FINISHED Shuffle Partitions")
    # # spark.stop()
