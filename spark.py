from pysbr import *
from datetime import datetime
from pyspark.sql.functions import col
from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext  
from pyspark.streaming import StreamingContext, StreamingListener

#eid = #whichever EVENT user has selected from dropdown
#mid = #whichever MARKET user has selected from dropdown

eid= 4667517
mid= 401

conds = 'event_id='+str(eid)+ " & " + 'market_id='+str(mid)

spark = SparkSession \
    .builder \
    .appName("betdata") \
    .getOrCreate()
    
cldf = spark.read \
     .format("org.apache.spark.sql.cassandra") \
     .options(table="currentlines", keyspace="betdata") \
     .load()

cldf.filter((col("result")=='W') & (col("market_id"))==(mid & col("event_id")==eid)) \
     .select(col("participant"), col("sportsbook"), col("american_odds"), col("inverse_odds"), col("profit")) \
     .sort(col("inverse_odds")) \
     .show()
