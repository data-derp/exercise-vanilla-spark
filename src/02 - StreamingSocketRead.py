from config.spark import init_spark, get_socket_stream

if __name__ == "__main__":
    spark = init_spark("PySpark Streaming Socket Read")

    # Create DataFrame representing the stream of input lines from connection to localhost:9999
    # This acts like the source of data

    lines_df = get_socket_stream(spark)
    # linesDF.show

    # This is like writing the data to the sink, console in this case
    query = lines_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()
