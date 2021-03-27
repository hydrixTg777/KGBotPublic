import time
from pyrogram import Client as app, filters
import asyncio
from asyncio import sleep
class Main():
	des = "Показывает время работы бота"
	cmd_list = {"uptime" : "понятно думаю"} 
	in_help = "uptime"

timer = time.time()

def uptime():
  now = time.time() - timer
  return int(now)

@app.on_message(filters.me & filters.command("uptime","."))
async def uptimer(app, message):
  hours = int((uptime() - uptime() % 60) / 3600)
  minutes = uptime() - hours * 3600
  minutes = int((minutes - minutes % 60) / 60)
  seconds = int(uptime() % 60) 
  await message.edit(f"ЮБ работает уже {hours} час(ов), {minutes} минут(ы) и {seconds} секунд(ы)") 