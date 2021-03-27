import importlib

from pyrogram import Client as app, filters
import os
import time


def modules_list():
	return [
	    module[:-3] for module in os.listdir("modules")
	    if module.endswith(".py")
	]


#Список модулей
@app.on_message(filters.me & filters.command("help", "."))
def help_bot(app, msg):
	me = app.get_me()
	try:
		name_module = msg.text.split(maxsplit=1)[1]
		if name_module in modules_list():
			s = importlib.import_module(f"modules.{name_module}")
			try:
				des = s.Main.des
			except:
				des = "Неизвестно"
			try:
				ver = s.Main.ver
			except:
				ver = "Неизвестно"
			try:
				cmd_list = s.Main.cmd_list
				text_cmd = ""
				for i in cmd_list.keys():
					text_cmd += f"{i} - {cmd_list[i]}\n"
			except:
				text_cmd = "Неизвестно"
			text = f"Информация о модуле **{name_module}:**\n\nОписание:\n{des}\n\nВерсия:\n{ver}\n\nКоманды:\n{text_cmd}"
			msg.edit(text)
		else:
			msg.edit(f"Модуль **{name_module}** не найден!")
	except IndexError:
		moduls = modules_list()
		text = f"**[KGBot](tg://user?id={me.id}) | [Канал](tg://resolve?domain=testy_ahaahahhahah)\nВведите .help [module] чтобы получить информацию о модуле\n\nДоступные модули:**\n"
		lenght = 0
		for i in moduls:
			s = importlib.import_module(f"modules.{i}")
			try:
				krat_help = s.Main.in_help
			except:
				krat_help = None
			if i == "basic":
				lenght -= 1
			else:
				text += f"• **{i}**: ```{krat_help}```\n"
			lenght += 1
		text += f"\nВсего модулей: **{lenght}**"
		msg.edit(text)


@app.on_message(filters.reply & filters.me & filters.command("loadmod", "."))
def load(app, message):
	name = message.reply_to_message.document.file_name
	doc = message.reply_to_message.document.file_id
	message.edit("**Установка модуля...**")
	app.download_media(message=doc, file_name=f"modules/{name}")
	message.edit("**Модуль установлен**")
	app.restart(False)
	time.sleep(1.5)
	message.delete()


def modules_list():
	for i in os.listdir("modules/"):
		if i.endswith(".py"):
			i = i.split(".")[0]
			yield i


@app.on_message(filters.me & filters.command("dlmod", "."))
def delete_module(app, msg):
	try:
		name = msg.text.split(maxsplit=1)[1]
		name = name.replace(" ", "_")
		if name in modules_list():
			os.popen(f"rm modules/{name}.py")
			msg.edit(f"Модуль **{name}** удалён!")
		else:
			msg.edit(f"Модуль **{name}** не найден!")
	except:
		msg.edit("Не указано имя модуля")
	app.restart(False)
	msg.delete()
