import os
from slack_sdk import WebClient

slack_token = os.environ.get("SLACK_TOKEN")

def send_slack_message(message):
    # Set up a WebClient with the Slack OAuth token
    client = WebClient(token=slack_token)

    # Send a message
    client.chat_postMessage(
        channel="gas-prices",
        text=message,
        username="rpi",
    )
