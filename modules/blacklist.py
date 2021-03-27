from pyrogram import Client as app, filters
import asyncio
class Main():
	in_help = "bl, unbl"
	des = "Кидает/убирает чела в/из чёрного списка по реплаю" 
	cmd_list = {
	"bl" : "кинуть в чс", 
	"unbl" : "убрать из чс"} 

@app.on_message(filters.me & filters.command('bl', '.'))
async def block(app, message):
	reply_id = message.reply_to_message.from_user.id
	name = message.reply_to_message.from_user.first_name
	await app.block_user(reply_id)
	await message.reply(f'Теперь {name} в чс')


@app.on_message(filters.me & filters.command('unbl', '.'))
async def unblock(app, message):
	reply_id = message.reply_to_message.from_user.id
	name = message.reply_to_message.from_user.first_name
	await app.unblock_user(reply_id)
	await message.reply(f'Теперь {name} не в чс')