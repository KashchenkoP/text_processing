import os
import findspark
findspark.init('/usr/local/spark/')
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-10_2.12:2.4.0 pyspark-shell'
sc = SparkContext(appName="PythonSparkStreamingKafka")
sc.setLogLevel("WARN")
ssc = StreamingContext(sc,60)
print('ssc =================== {} {}');
kafkaStream = KafkaUtils.createStream(ssc, 'localhost:2181', 'spark-streaming', {'mongo':0})
print('contexts =================== {} {}');
lines = kafkaStream.map(lambda x: x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()


# def decoder(msg):
#     baseMessage = json.loads(zlib.decompress(msg[4:]))
#     message = {"headers": baseMessage["headers"],
#                "data": b64decode(baseMessage["data"])}
#     return message

