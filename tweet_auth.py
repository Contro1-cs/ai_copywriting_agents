import requests
import time
import random
import hashlib
import hmac
import base64
from urllib.parse import quote

# Replace these variables with your actual credentials
consumer_key = 'IFYWCTUzYQI5wgeu0DQxuH9NO'
consumer_secret = '0FqMP3M3cNmUQnv1IJpUcXdkIxdGLlKi9qj2kc3zTmiWPLXEuL'
access_token = '1709219596626960385-YRxziQ03QKGjuegiWdZA44ClfrleTL'
access_token_secret = 'RUHBGqhhCxjA7vmYo7zB7hxek22C16XOnjdVd0kSVHUM2'

# Parameters for the OAuth signature
oauth_nonce = ''.join([str(random.randint(0, 9)) for i in range(8)])
oauth_timestamp = str(int(time.time()))
status = "Hello world"

# Creating the OAuth signature base string
base_info = f"oauth_consumer_key={consumer_key}&oauth_nonce={oauth_nonce}&oauth_signature_method=HMAC-SHA1&oauth_timestamp={oauth_timestamp}&oauth_token={access_token}&oauth_version=1.0&status={quote(status)}"
base_string = f"POST&{quote('https://api.twitter.com/1.1/statuses/update.json', safe='')}&{quote(base_info, safe='')}"

# Creating the signing key
signing_key = f"{quote(consumer_secret)}&{quote(access_token_secret)}"

# Creating the OAuth signature
hashed = hmac.new(signing_key.encode(), base_string.encode(), hashlib.sha1)
oauth_signature = base64.b64encode(hashed.digest()).decode()

# Construct the authorization header
auth_header = (
    f'OAuth oauth_consumer_key="{consumer_key}", '
    f'oauth_nonce="{oauth_nonce}", '
    f'oauth_signature="{quote(oauth_signature)}", '
    f'oauth_signature_method="HMAC-SHA1", '
    f'oauth_timestamp="{oauth_timestamp}", '
    f'oauth_token="{access_token}", '
    f'oauth_version="1.0"'
)

# URL for the request
url = 'https://api.twitter.com/1.1/statuses/update.json'

# Parameters for the request
params = {'status': status}

# Making the request
response = requests.post(url, headers={'Authorization': auth_header}, params=params)

# Check the response
if response.status_code == 200:
    print("Tweet posted successfully!")
else:
    print(f"Failed to post tweet: {response.status_code}, {response.text}")
