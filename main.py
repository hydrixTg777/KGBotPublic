from pyrogram import Client
import os

app = Client("account", api_id = 6, api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e", plugins = dict(root = "modules"))

app.run()
	
