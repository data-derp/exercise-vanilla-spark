from pyspark.sql import *
from lib.logger import Log4j


if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Hello Spark") \
        .getOrCreate()

    logger = Log4j(spark)

    logger.info("Start Long Spark Program")
    ds1 = spark.range(1, 10000000)
    ds1.cache()
    ds1.count()
    ds1.show()

    ds2 = spark.range(1, 10000000)
    # ds2.cache()
    ds2.count()
    ds2.show()
    # ds3 = ds1.repartition(7)
    # ds3.cache()
    # # ds3.show()
    # ds3.count()
    # ds4 = ds2.repartition(9)
    # ds5 = ds1.selectExpr("id * 5 as id")
    # # # ds5 = ds3.selectExpr("id * 5 as id")
    # joined = ds5.join(ds2, "id")
    # joined.show()
    # # # joined = ds5.join(ds4, "id")
    # # # joined = ds1.join(ds2)
    joined = ds1.join(ds2)
    # sumOfIds = joined.selectExpr("sum(id)")
    # sumOfIds.show()
    joined.show()

    input("Please Input..")

    logger.info("Finished Long Spark Program")
    spark.stop()
