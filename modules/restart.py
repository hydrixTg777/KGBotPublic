from pyrogram import Client as app, filters

class Main():
	des = "Перезагружает бота"
	in_help = "restart"
	cmd_list = {"restart" : "перезагрузка"} 

@app.on_message(filters.me & filters.command("restart", "."))
def restart_bot(app, msg):
	msg.edit("**Перезагрузка...**")
	app.restart(False)
	msg.edit("**Перезагрузка прошла успешно!**")