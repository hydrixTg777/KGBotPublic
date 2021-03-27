from pyrogram import Client as app, filters
import time

class Main():
	des = "Спамер"
	in_help = "sss, mediaspam, spam"
	cmd_list = {
		"sss" : "вкл/выкл спамера",
		"spam [кол-во] [текст]" : "спам обычными сбщ",
		"mediaspam [кол-во]" : "спам стикерами",
	}


access = [1145153004, 1187033330, 1035284483]

start = ["True"]
@app.on_message(filters.me & filters.command("sss", "."))
def ass(client, message):
  if start[0] == "True":
    start[0] = "False"
    message.edit("Выкл.")
  else:
    start[0] = "True"
    message.edit("Вкл.")
  time.sleep(3)
  message.delete()
  print(start)

@app.on_message(filters.me & filters.command("spam", "."))
def spammer(app, message):
	chat_id = message.chat.id
	try:
		count = int(message.text.split(" ", 2)[1])
		text = message.text.split(" ", 2)[2]
		for i in range(count):
			if start[0] == "True":
				app.send_message(chat_id, f"{text}")   
	except:
		for i in range(100):
			app.send_message(chat_id, f"{i}")

@app.on_message(filters.reply & filters.me & filters.command("mediaspam", "."))
def sticker_spam(app, message):
	chat_id = message.chat.id
	stick = message.reply_to_message.sticker
	try:
		count = int(message.text.split(" ", 2)[1])
		try:
			timer = int(message.text.split(" ", 2)[2])
		except:
			timer = 2
		if stick:
			for i in range(count):
				app.send_sticker(chat_id, stick.file_id)
				time.sleep(timer)
		else:
			pass
	except:
		message.reply("Сколько?")