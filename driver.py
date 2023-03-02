def create_sparksession():
    """
    Initialize a spark session
    """
    return SparkSession.builder.master('yarn').appName("bettor") \
           .config("spark.jars.packages","saurfang:spark-sas7bdat:2.0.0-s_2.11") \
           .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.2") \
           .enableHiveSupport()
           .getOrCreate()