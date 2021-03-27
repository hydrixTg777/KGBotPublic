from pyrogram import Client as app, filters

class Main():
	des = "Ливает из чата"
	in_help = "leave"

@app.on_message(filters.me & filters.command("leave", "."))
def leaver(app, message):
	chat_id = message.chat.id
	try:
		text = message.text.split(" ", 1)[1]
		message.edit(f"**{text}**")
	except:
		message.edit("**До связи**")
	app.leave_chat(chat_id)
