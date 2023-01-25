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
    # ratings_df = spark.read.csv(file_path1)
    # ratings_df.show(truncate=False)

    # In fact it will be the same when you keep header equal to true
    # ratings_df = spark.read \
    #     .option("header", "True") \
    #     .csv(file_path1)
    # #
    # ratings_df.show(truncate=False)

    # should show to 2 jobs because of the header and infer schema extra processing
    # ratings_df = spark.read \
    #     .option("inferSchema", "True") \
    #     .option("header", "True") \
    #     .csv(file_path1)

    # ratings_df.show(truncate=False)

    # now lets read a bigger csv file
    file_path2 = f"{DATA_DIR}/TemperaturesByCountry.csv"

    # A simple read will work the same way as above
    # temp_df = spark.read.csv(file_path2)
    #
    # # # # # Ditto for the show
    # temp_df.show(truncate=False)

    # However, the spark UI will show 2 jobs, one of the header true and other for the inferSchema
    # when you add the inferSchema option
    # temp_df = spark.read \
    #     .option("header", "True") \
    #     .option("inferSchema", "True") \
    #     .csv(file_path2)

    # show as before will add a job with one task
    # temp_df.show(truncate=False)

    # Let us check count too, it should give you the count of all the rows
    # However, the count will show 5 tasks, for the partition totals
    # and one for the shuffle for the communication across the network
    # which gives and final result
    # print(temp_df.count())

    # collect will show all data in Spark UI and 4 tasks
    # Be careful about collect as it can overwhelm the machines from which
    # you are running your program
    # You will also observe that collect will show as 4 tasks not as 5 as was the case
    # with count because the count is doing and extra task of counting whereas collect is just
    # returning the data from individual partitions
    # print(temp_df.collect())

    # Let us look at json dataset too. For jSON, the data will be read at once for all
    # the partitions. That's how jSON works with spark
    file_path3 = f"{DATA_DIR}/iot_devices.json"
    json_df = spark.read.json(file_path3)
    json_df.show()

    input("Please ENTER")

    logger.info("Finished Spark File Read")
    spark.stop()
