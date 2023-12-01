import schedule
import time
from slack import WebClient
from slack.errors import SlackApiError

# Replace 'YOUR_BOT_TOKEN' with your actual Slack bot token
SLACK_BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL_ID = 'YOUR_CHANNEL_ID'

def send_standup_message():
    standup_message = (
        "Hey team! It's standup time. Please answer the following questions:\n"
        "1. What did you work on yesterday?\n"
        "2. What are you working on today?\n"
        "3. Are there any blockers?"
    )

    client = WebClient(token=SLACK_BOT_TOKEN)

    try:
        response = client.chat_postMessage(channel=CHANNEL_ID, text=standup_message)
        print("Standup message sent successfully!")
    except SlackApiError as e:
        print(f"Error sending standup message: {e.response['error']}")

# Replace 'HH:MM' with the desired time for the standup meeting
schedule.every().day.at('09:00').do(send_standup_message)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    run_scheduler()