import requests
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox107dd4345e25468bb6ebc6de45b4f426.mailgun.org/messages",
        auth=("api", "key-623227bd997408488d172bc16d50d6c1"),
        data={"from": "Breakfaster <mailgun@sandbox107dd4345e25468bb6ebc6de45b4f426.mailgun.org>",
              "to": ["juliabondtv@gmail.com"],
              "subject": "Hello Backpacker",
              "text": "Hello Traveler with Taste, Welcome to the website that brings the world to your breakfast table, we look forward to having you along for the journey, Best team BB"})
send_simple_message()