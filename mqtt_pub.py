# -*- coding: cp1252 -*-
import paho.mqtt.client as mqtt
from struct import pack
from random import randint
from time import sleep

from libsoc_zero.GPIO import Button


btn = Button('GPIO-A')

# topicos providos por este sensor
TOPIC = "digital" 


# cria um identificador baseado no id do sensor
client = mqtt.Client(client_id = 'Teste' ,
                     protocol = mqtt.MQTTv31)

client.will_set('casa/will', 'Last will', 0, False)

# conecta no broker
client.connect("192.168.0.14", 1883)


while True:
    sleep(0.25)
    if btn.is_pressed():
        client.publish(TOPIC,"ON",qos=0)
    else:
        client.publish(TOPIC,"OFF",qos=0)


sleep(5)
client.disconnect()


