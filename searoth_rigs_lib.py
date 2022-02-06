import requests
import time
import datetime
import uuid
import hmac
import json
import sys
from hashlib import sha256

config_file = open('config.json')
config = json.load(config_file)

public_api_key = config['public_api_key']
private_api_key = config['private_api_key']
organization_id = config['organization_id']


def log_time():
    return "[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] "


def api_call(method, path, query, body):
    xTime = str(round(time.time() * 1000))
    xNonce = str(uuid.uuid4())

    message = bytearray(public_api_key, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(xTime, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(xNonce, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(organization_id, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(method, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(path, 'utf-8')
    message += bytearray('\x00', 'utf-8')
    message += bytearray(query, 'utf-8')

    if body:
        json_body = json.dumps(body)
        message += bytearray('\x00', 'utf-8')
        message += bytearray(json_body, 'utf-8')

    signature = hmac.new(bytearray(private_api_key, 'utf-8'),
                         message, sha256).hexdigest()

    xAuth = public_api_key + ":" + signature

    headers = {
        'X-Time': xTime,
        'X-Nonce': xNonce,
        'X-Organization-Id': organization_id,
        'X-Request-Id': str(uuid.uuid4()),
        'X-Auth': xAuth,
        'Content-Type': 'application/json'
    }

    s = requests.Session()
    s.headers = headers

    if body:
        response = s.request(
            method, "https://api2.nicehash.com" + path, data=json_body)
    else:
        response = s.request(method, "https://api2.nicehash.com" + path)

    return response

def get_rigs():
    reply = api_call(
        "GET", "/main/api/v2/mining/rigs2", "", None)
    return json.loads(reply.content)    

def get_stopped_rigs():
    stopped_rigs = []
    response = get_rigs()
    for r in response['miningRigs']:
        minerStatus = r['minerStatus']
        if minerStatus == "STOPPED":
            stopped_rigs.append(r['rigId'])
    return stopped_rigs

def get_mining_rigs():
    mining_rigs = []
    response = get_rigs()
    for r in response['miningRigs']:
        minerStatus = r['minerStatus']
        if minerStatus == "MINING":
            mining_rigs.append(r['rigId'])
    return mining_rigs
