from config.definitions import DATA_DIR
from config.spark import init_spark
from lib.logger import Log4j

if __name__ == "__main__":
    spark = init_spark("BucketsBy Example")

    conf = spark.conf
    # conf.set("spark.sql.shuffle.partitions", 2)
    conf.set("spark.master", "local[8]")

    logger = Log4j(spark)

    logger.info("STARTED Spark Buckets")

    # reading JSON file
    file_path = f'{DATA_DIR}/plane-data.csv'

    data = spark.read \
        .option('header', True) \
        .csv(file_path)

    # data2 = data.select(*[col for col in data.columns if col not in ['year']], data.year.cast('integer'))
    # data2.show(20)
    # #
    numberOfBucket = 4
    columnToBucketBy = 'year'
    data.write.mode("overwrite").format('csv').bucketBy(numberOfBucket, columnToBucketBy)\
        .saveAsTable('bucketedFiles')

    input("Please enter..")
    #
    # logger.info("FINISHED Spark Buckets")
    spark.stop()
