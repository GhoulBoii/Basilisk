import os
from requests import get

# TODO: add more versions
# TODO: check if windows or linux
# TODO: add playit support
# TODO: add mods/plugins support

name = ""
directory = ""
version = ""
server = ""

def input_values():
    print("Enter your choices below. Options marked with * are the default.")
    global name, directory, version, server
    name = input("Enter the name of the minecraft server: ")
    directory = input("Where do you want to install your server?: ")
    version = input("Enter version number you want to use: (1.20.1*, 1.19.1): ")
    server = input("Enter what server you want: (purpur*, paper, vanilla): ")
    
    if not version:
        version = "1.20.1"
    if not server:
        server = "purpur"

def changing_path():
    path = os.path.join(directory,name)
    os.mkdir(path)
    os.chdir(path)


def installing_jar():
    match server:
        case "purpur":
            response = get(f"https://api.purpurmc.org/v2/purpur/{version}/latest/download")
        case "paper":
            api = "https://papermc.io/api/v2/projects/paper"
            headers = {"accept":"application/json"}
            link = get(f"{api}/version_group/{version}/builds", headers = headers).json()["builds"][-1]
            response = get(f"{api}/versions/{link['version']}/builds/{link['build']}/downloads/paper-{link['version']}-{link['build']}.jar")
        case "vanilla":
            link = get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"]
            for i in link:
                if i['id'] == version:
                    response = get(get(i['url']).json()["downloads"]["server"]["url"])
        case _:
            print("Wrong input")

    with open("server.jar","wb") as file:
        file.write(response.content)

def accept_eula():
    with open("eula.txt","w") as file:
        file.write("eula=true")

input_values()
changing_path()
installing_jar()
accept_eula()
 
print("Server has been installed without errors. Just run run.py and the server will start. Enjoy!")