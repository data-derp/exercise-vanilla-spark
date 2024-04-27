from os import environ

from pyspark.sql import SparkSession


def init_spark(app_name: str) -> SparkSession:
    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    return spark


def get_socket_stream(spark: SparkSession):
    streaming_app = environ.get('STREAMING_APP_HOST', "localhost")
    print(f"Streaming App: {streaming_app}")

    return spark.readStream \
        .format("socket") \
        .option("host", streaming_app) \
        .option("port", 9999) \
        .load()