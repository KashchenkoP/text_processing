from datetime import datetime, timedelta
import time
import json
import threading
import logging

from pymongo import MongoClient
from kafka import KafkaProducer

import configure

#logging.basicConfig(level=logging.DEBUG)
mogo_cli = MongoClient(configure.mongo_connection_url)
kafka_producer = KafkaProducer(bootstrap_servers=['35.204.164.2:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def get_posts_cursor(from_time, cli):
    collection = cli.test.posts
    return collection.find({
        "event_date_store": {
            "$gt": from_time,
        }
    }).sort("event_date_store", 1)


def send_to_kafka(value, kafka_producer):
    return kafka_producer.send("mongo", value=value)


if __name__ == '__main__':
     from_time = datetime.now() - timedelta(hours=3.0)
     while True:
         for post in get_posts_cursor(from_time, mogo_cli):
             from_time = post.get('event_date_store')
             post["_id"] = str(post.get("_id"))
             post["event_date_store"] =  str(post.get("event_date_store"))
             post["event_date_updated"] = str(post.get("event_date_updated"))
             post["event_date"] = str(post.get("event_date"))
             send_to_kafka(post, kafka_producer=kafka_producer)
         time.sleep(2.0)
