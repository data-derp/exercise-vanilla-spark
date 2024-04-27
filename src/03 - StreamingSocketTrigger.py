from config.spark import init_spark, get_socket_stream

if __name__ == "__main__":
    spark = init_spark("PySpark Streaming Socket Read")

    # Create DataFrame representing the stream of input lines from connection to localhost:9999
    # This acts like the source of data
    linesDF = get_socket_stream(spark)

    # This is like writing the data to the sink, console in this case
    query = linesDF \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .trigger(processingTime='15 seconds') \
        .start()

    query.awaitTermination()
