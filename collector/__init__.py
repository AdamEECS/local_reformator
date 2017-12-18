from config.key import headers, url_base
from models.product import Product
import time
import json
import requests
import os
from pyquery import PyQuery as pq
from usr_util.utils import timestamp, time_str, log
import pyglet

path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(path, '..', 'static', 'alarm01.mp3')
alarm = pyglet.media.load(file)


def log_path():
    print(path)


def timer(delta, procedure):
    while True:
        try:
            procedure()
        except BaseException as e:
            log('error', e)
        time.sleep(delta)
