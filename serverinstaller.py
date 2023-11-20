import os
from requests import get

NAME = ""
DIR = ""
VERSION = ""
SERVER = ""

def input_name():
    name = input("Enter the name of the minecraft server: ")
    return name

def input_dir():
    direc = input("Where do you want to install your server?: ")
    return direc

def input_version():
    version = input("Enter version number you want to use: (1.20.1*, 1.19.1): ")
    if not version:
        version = "1.20.1"
    return version

def input_server():
    server = input("Enter what server you want: (purpur*, paper, vanilla): ")
    if not server:
        server = "purpur"
    return server

def changing_path():
    path = os.path.join(DIR,NAME)
    os.mkdir(path)
    os.chdir(path)

def installing_jar():
    match SERVER:
        case "purpur":
            response = get(f"https://api.purpurmc.org/v2/purpur/{VERSION}/latest/download", timeout = 10)
        case "paper":
            api = "https://papermc.io/api/v2/projects/paper"
            headers = {"accept":"application/json"}
            link = get(f"{api}/version_group/{VERSION}/builds", headers = headers, timeout = 10).json()["builds"][-1]
            response = get(f"{api}/versions/{link['version']}/builds/{link['build']}/downloads/paper-{link['version']}-{link['build']}.jar", timeout = 10)
        case "vanilla":
            link = get("https://launchermeta.mojang.com/mc/game/version_manifest.json", timeout = 10).json()["versions"]
            for i in link:
                if i['id'] == VERSION:
                    response = get(get(i['url'], timeout = 10).json()["downloads"]["server"]["url"], timeout = 10)
        case _:
            print("Wrong input")

    with open("server.jar", "wb") as file:
        file.write(response.content)

def accept_eula():
    with open("eula.txt", "w", encoding="utf-8") as file:
        file.write("eula=true")

print("Enter your choices below. Options marked with * are the default.")
NAME = input_name()
DIR = input_dir()
SERVER = input_server()
VERSION = input_version()
changing_path()
installing_jar()
accept_eula()

print("Server has been installed without errors. Just run run.py and the server will start. Enjoy!")

