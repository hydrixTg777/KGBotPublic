from pyrogram import Client as app, filters
import os
import time


def tran(money, kof):
	try:
		res = [i for i in money if str(i) in "1234567890"]
		bukva = [i for i in money if str(i) not in "1234567890"]
		return str(int(''.join(res)) * int(kof)) + ''.join(bukva)
	except:
		pass

def check_at_letter(stavk):
	return int(''.join([i for i in stavk if str(i) in '1234567890']))

gamemode = [False]
start_stavka = ["10мк"]
stavka = ['10мк']
linia = [0]
jeck = [0]
fail = [0]
para =  [0]
vozv = [0]
kf = [3]

#включение
@app.on_message(filters.me & filters.command("sloton","."))
def slot_on( app, msg):
	if gamemode[0] == True: gamemode[0] = False; msg.edit("Выкл")
	else: gamemode[0] = True; msg.edit("Вкл")
	try:
		stavka1 = msg.text.split(" ")[1]
		stavka[0] = stavka1
		start_stavka[0] = stavka[0]
		try:
			kof = int(msg.text.split(" ")[2])
			kf[0] = kof
		except:
			pass
	except:
		stavka[0] = start_stavka
	time.sleep(2)
	app.send_message(msg.chat.id, f"Слот {stavka[0]}")
	

#проверка состояния игрового бота
@app.on_message(filters.me & filters.command("checks","."))
def check_bot( app, msg):
	msg.edit(f"""Начальная ставка: {start_stavka[0]}
Нынешняя ставка: {stavka[0]}
Пара: {para[0]}
Линия: {linia[0]}
Джекпот: {jeck[0]}
Возврат: {vozv[0]} 
Проигрыш: {fail[0]}
Кф: {kf[0]}""")


#возврат
@app.on_message(filters.bot & ~filters.me & filters.edited & filters.regex("Возврат!"))
def return_money( app, msg):
	if msg.chat.id == 1097604479:
		if gamemode[0]:
			app.send_message(msg.chat.id, f"Слот {stavka[0]}")
			vozv[0] +=  1


#пара
@app.on_message(filters.bot & ~filters.me & filters.regex("Пара!") & filters.edited)
def win2x( app, msg):
	if msg.chat.id == 1097604479:
		if gamemode[0]:
			para[0] += 1
			stav = int(str(msg.text).split("забирай")[-1].replace(" ", ""))
			delit = check_at_letter(stavka[0])
			res = stav / delit
			for_graph.append(for_graph[-1] + float(res))
			stavka[0] = start_stavka[0]
			app.send_message(msg.chat.id, f"Слот {stavka[0]}")


#линия
@app.on_message(filters.bot & ~filters.me & filters.edited & filters.regex("Линия!"))
def win5x( app, msg):
	if msg.chat.id == 1097604479:
		if gamemode[0]:
			linia[0] += 1
			stav = int(str(msg.text).split("забирай")[-1].replace(" ", ""))
			delit = check_at_letter(stavka[0])
			res = stav / delit
			for_graph.append(for_graph[-1] + float(res))
			stavka[0] = start_stavka[0]
			app.send_message(msg.chat.id, f"Слот {stavka[0]}")

#джекпот
@app.on_message(filters.bot & ~filters.me & filters.edited & filters.regex("ДЖЕКПОТ!"))
def win50x( app, msg):
	if msg.chat.id == 1097604479:
		if gamemode[0]:
			stavka[0] = start_stavka[0]
			app.send_message(msg.chat.id, f"Слот {stavka[0]}")
			jeck[0] += 1
			for_graph.append(for_graph[-1] + 100)

#проигрыш
@app.on_message(filters.bot & ~filters.me & filters.edited & filters.regex("Упс тебе попался крестик!") | filters.regex("Попробуй еще раз!"))
def fail2( app, msg):
	if msg.chat.id == 1097604479:
		if gamemode[0]:
			test_stavka = stavka[0]
			stavka[0] = tran(test_stavka,kf[0])
			app.send_message(msg.chat.id, f"Слот {stavka[0]}")
			fail[0] += 1

			for_graph.append(for_graph[-1] - 1)

