from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import time
# api_id and api_hash from https://my.telegram.org/apps

api_id = 17387947
api_hash = '20727f8a7430b3957726eb876bb16a4b'
phone = '+2001030589557'
count = 0
SLEEP_TIME = 7320
while (count < 3):
	client = TelegramClient('user', api_id, api_hash).start()

	# This message can contain any text, links, and emoji:
	message  = ("🎁 الهدية")

	receiver = client.get_input_entity('https://t.me/FreeCoin_MoneyBOT')
	client.send_message(receiver, message)
	time.sleep(SLEEP_TIME)

