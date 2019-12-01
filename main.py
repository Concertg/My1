import os
import time as tm
import requests as rs
import json as js
import webbrowser as web
login = "Concertg"
email = "sasha.noskov.2227@mail.ru"
repository = "My1"
print('-' * 70)
password = input("Ведите пароль: ")
print("\033[A" + 'Ведите пароль: ', '*' * len(password))

if os.name == "nt":
    path = "fi"
else:
    path = "/home/algoritmika/Документы"

url = "https://api.github.com/user/repos"
auth = (login, password)
data = {
    "name": f"{repository}",
    "description": "python"}
repos = rs.get(url, auth=auth)
if repos.status_code == 200:
    print("[INFO]вход выполнен")
else:
    print("[ERROR] вход не вполнен")
new_repository = rs.post(url, auth=auth, data=js.dumps(data))
for repo in repos.json():
    print(repo["html_url"])
os.chdir(path)
_, folder = os.path.split(os.getcwd())
os.system(f"git clone https://github.com/{login}/{repository}.git")
os.chdir(f'{path}/{repository}')
os.system(f'git config user.email "{email}" && git config user.name "{login}" && git remote set-url origin https://{login}:{password}@github.com/{login}/{repository}.git')
f = open('main.py', 'a')
f.close()
print(f'[INFO] Выход\n{"-" * 70}')
tm.sleep(2)
web.open(f'https://github.com/{login}')