import aiohttp
import random
import settings

webhook_urls = settings.ANON_WEBHOOK
# Define the async send_message function that takes 'content' as an argument
async def send_message(content):
    # Create a dictionary 'payload' with a key 'content' and the provided content
    payload = {'content': content}

    # Shuffle the 'webhook_urls' list to select a random webhook URL
    random.shuffle(webhook_urls)

    # Get the first (random) webhook URL from the shuffled list
    webhook_url = webhook_urls[0]

    # Initialize an aiohttp ClientSession
    async with aiohttp.ClientSession() as session:
        # Send a POST request to the selected webhook URL with the payload
        async with session.post(webhook_url, json=payload) as response:
            # Check if the response status code is 200 (OK)
            if response.status == 204:
                return
            else:
                print(f"Failed to send message. Status code: {response.status}")