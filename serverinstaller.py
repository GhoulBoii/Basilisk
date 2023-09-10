import os
import subprocess
from requests import get

os = os.name
server,version,playit = "purpur","1.20.1","no"

# TODO: add more versions
# TODO: check if windows or linux
# FIX: Default Options
print("Enter your choices below. Options marked with * are the default.")
name = input("Enter the name of the minecraft server: ")
directory = input("Where do you want to install your server?: ")
version = input("Enter version number you want to use: (1.20.1*, 1.19.1): ")
server = input("Enter what server you want: (purpur*, paper, vanilla): ")
# playit = input("Do you want to use playit?: ")
# mod = input("Enter mods or plugins you want to use: ")

path = os.path.join(path,name)
os.mkdir(path)
os.chdir(path)

def installing_jar():
    match server:
        case "purpur":
            response = get(f"https://api.purpurmc.org/v2/purpur/{version}/latest/download")
        case "paper":
            headers = {"accept":"application/json"}
            link = get(f"https://paper.mc.io/api/v2/projects/paper/version_group/{version}/builds", headers = headers).json()["builds"][-1]
            response = get(f"https://papermc.io/api/v2/projects/paper/versions/{link['version']}/builds/{link['build']}/downloads/paper-{link['version']}-{link['build']}.jar")
        case "vanilla":
            link = get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"]
            for i in link:
                if i['id'] == version:
                    response = get(get(i['url']).json()["downloads"]["server"]["url"])
        case _:
            print("Wrong input")
            
    with open("server.jar","wb") as file:
        file.write(response.content)
    
installing_jar()
with open("eula.txt",w) as file:
    file.write("eula=true")
    
print("Server has been installed without errors. Just run run.py and the server will start. Enjoy!")