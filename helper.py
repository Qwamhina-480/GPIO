import requests
from gpiozero import Button
from signal import pause

button = Button(3)

WEBHOOK_URL = "https://qwamhina.app.n8n.cloud/webhook-test/e5ba8906-e428-48bb-9c2e-df8190ebef99"
def send_email():
    print("Button pressed")
    requests.get(WEBHOOK_URL)

button.when_pressed = send_email

print("Waiting for button press.... ")
pause()