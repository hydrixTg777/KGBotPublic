id = int(input("Введите api_id: "))
hash = input("Введите api_hash: ")

with open("config.ini","w+") as f:
	f.write(f"""[pyrogram]
lang_code = ru
app_version = 1.0
device_model = Linux
system_version = Linux
api_id = {id}
api_hash = {hash}

[plugins]
root = modules
""")