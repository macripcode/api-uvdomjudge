#!/usr/bin/env python
# -*- coding: utf-8 -*-.

import pika
import requests
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue_create_user')


def create_user(user):
    url = "http://127.0.0.1:8001/uv-domjudge/v1/users/"
    response = requests.post(url=url, json=user)
    return response.status_code


def on_request(ch, method, props, body):
    user = json.loads(body.decode('utf-8'))
    response = create_user(user)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='queue_create_user')

print(" [x] Awaiting RPC requests")
channel.start_consuming()