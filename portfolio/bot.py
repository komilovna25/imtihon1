import requests

from config.settings import CHAT_ID, BOT_TOKEN


def  send_message(text):
  BOT_TOKENs = BOT_TOKEN
  CHAT_IDs = CHAT_ID
  PHOTO = "https://png.pngtree.com/thumb_back/fh260/background/20230612/pngtree-the-sun-sets-over-the-ocean-with-waves-image_2967426.jpg"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKENs}/sendphoto?chat_id={CHAT_IDs}&photo={PHOTO}&caption={TEXT}"
  response = requests.get(url)


  if response.status_code == 200:
        print("Message sent successfully to Telegram bot!")
  else:
        print(f"Failed to send message. Status code: {response.status_code}")
