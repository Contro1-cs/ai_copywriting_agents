import requests
import json

# Replace this with your actual Bearer Token
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAKz8twEAAAAAcO6zIJ2I7QpZWl23OsDdIJnNSPE%3DEsEmhnxFSEGLAWLeUIfkNi8om0XgyTqgpzQMDlRyMley7xZ5Pz'

# URL for the request
url = 'https://api.twitter.com/2/tweets'

# Tweet data
tweet_data = {
    "text": "I tweeted this using X's API!"
}

# Headers for the request
headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json'
}

# Making the request
response = requests.post(url, headers=headers, data=json.dumps(tweet_data))

# Check the response
if response.status_code == 201:
    print("Tweet posted successfully!")
else:
    print(f"Failed to post tweet: {response.status_code}, {response.text}")
