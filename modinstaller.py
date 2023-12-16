import os
from requests import get
from serverinstaller import DIR,VERSION,PATH,changing_path

print(DIR,VERSION,PATH)
mods = ["sodium", "iris"]

def input_dir():
    dir = input("Enter server dir: ")
    return dir

changing_path(PATH,"mods")

for i in mods:
    response = get(get(f"https://api.modrinth.com/v2/project/{i}/version?game_versions=[\"{VERSION}\"]").json()[0]["files"][0]["url"])
    open(f"{i}.jar","wb").write(response.content)

