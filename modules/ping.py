from pyrogram import Client as app , filters
import time

class Main():
	des = "Пинг"
	in_help = "p"

@app.on_message(filters.command("p", ".") & filters.me, group = 2)
async def ping1_1(app, message):
    start = time.time()
    reply = await message.edit("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**Пинг: ** `{delta_ping * 1000:.2f} мс`")