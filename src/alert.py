import requests
import json

def send_slack_alert(webhook, message):
    payload = {"text": message}
    requests.post(webhook, data=json.dumps(payload))