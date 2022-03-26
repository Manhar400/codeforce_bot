import requests
def send_message(message):
    TOKEN = "52512392XXXXXXXXXXXXXXXXXXXXX_ORkNEwqLWcMJjU"
    chat_id = "XXXXX4541"
    send_text = message
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={send_text}"
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    r = requests.get(url)
