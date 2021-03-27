from pyrogram import Client, filters
import sys
import os
from io import StringIO
from meval import meval
import traceback

class Main:
	des = "Выполнение Python кода"
	ver = "2.0"
	cmd_list = {
		"eval + код": "выполнение"
	}
	in_help = "eval"

res = "**Код**:\n\n```{}```\n\n**Результат**:\n\n```{}```"

@Client.on_message(filters.command("eval", ".") & filters.me)
async def eval_func(app, msg):
	try:
		code = msg.text.split(maxsplit=1)[1]
	except:
		code = msg.reply_to_message.text
	logs = ''
	old_stdout = sys.stdout
	result = sys.stdout = StringIO()
	try:
		await meval(code, {"__name__":"", "__package__":""}, app=app, msg=msg)
	except:
		logs=traceback.format_exc(0)
	sys.stdout = old_stdout
	if logs:
		await msg.edit(res.format(code, logs))
	else:
		try:
			await msg.edit(res.format(code, result.getvalue()))
		except:
			await msg.edit(res.format(code, "[400 MESSAGE_TOO_LONG]"))