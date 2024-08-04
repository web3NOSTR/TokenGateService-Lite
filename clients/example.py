import requests
import json

# API endpoint
url = 'http://your-flask-app-url/verify-token'

# The message and signature to verify
data = {
    'message': 'Your message to sign',
    'signature': '0xYourSignature'
}

# Sending POST request
response = requests.post(url, json=data)

# Check for HTTP request errors
if response.status_code == 200:
    result = response.json()
    if result['success']:
        if result['holding']:
            print('The recovered address holds the token.')
        else:
            print('The recovered address does not hold the token.')
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")
else:
    print(f"Failed to reach the server. Status code: {response.status_code}")
