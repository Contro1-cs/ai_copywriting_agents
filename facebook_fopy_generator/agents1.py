import requests

def Agent1(name, query, expected_results):
    print(f'\033[0m{name} is Working...\033[0m')
    # Define the request payload
    if query == "Content not found":
        exit()
        
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Query:{query}\n\nExpected output: {expected_results}",
                    }
                ],
            }
        ]
    }

    # Define the headers
    headers = {
        "Content-Type": "application/json"
    }

    # Define the API endpoint
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyBdUzwBDPozaAmnw8P6uku2QlkoVeXCpWA"

    # Make the POST request
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the text from the response
        json_response = response.json()
        if 'content' in json_response['candidates'][0]:
            answer = json_response['candidates'][0]['content']['parts'][0]['text']
        else:
            answer = "Content not found"
        print(f'\033[92m{name} Completed\033[92m')
        return answer
    else:
        # Print error message if request fails
        print("Error:", response.text)
        return None 