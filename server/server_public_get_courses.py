#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import requests


PUBLIC_TOKEN = "Token 88a6ffd23a17643147f9497974e5125cd0463cd0"


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_get_courses')


def get_courses():
    url = "http://127.0.0.1:8001/uv-domjudge/v1/courses/"
    headers = {
        'content-type': "application/json",
        'authorization': PUBLIC_TOKEN
    }
    response = requests.get(url, headers=headers)
    return response.text


def on_request(ch, method, props, body):
    print("Get Current Courses")
    response = get_courses()
    print(response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response.encode('utf-8'))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_get_courses')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
