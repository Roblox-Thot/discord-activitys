import http.client, json

with open("json/detectable.json",'r+') as file:
    conn = http.client.HTTPSConnection("discord.com")

    conn.request("GET", "/api/v9/applications/detectable")

    res = conn.getresponse()
    data = res.read()

    old_data = json.load(file)
    new_data = json.loads(data.decode())

    old_names = [x['name'] for x in old_data]
    old_execs = [x['executables'] for x in old_data if "executables" in x]
    new_names = [x['name'] for x in new_data]
    new_execs = [x['executables'] for x in new_data if "executables" in x]

    execs_list = [y["name"] for x in new_execs for y in x]
    new_names.sort()
    execs_list.sort()
    names_text_list = ('\n').join(new_names)
    execs_text_list = ('\n').join(execs_list)
    open('text/games.txt','w').write(names_text_list)
    open('text/executables.txt','w').write(execs_text_list)

    # Print new names that are not in the old list
    added_games = [name for name in new_names if name not in old_names]
    added_execs = [name for name in new_execs if name not in old_execs]
    print("[Main]",f"{len(old_data)} -> {len(new_data)} games (+{len(new_data) - len(old_data)})")
    print("[Main] New games:",added_games)
    print("[Main] New executables:",len(added_execs))

    # Makes a temp file used for the commit messages
    commmit_msg = '(Apps update) Updated JSONs\n'
    for game in added_games:
        commmit_msg += f'- {game}\n'
    open('temp_commit.txt','w').write(commmit_msg)

    if len(added_games) or len(added_execs):
        file.seek(0)
        json.dump(new_data, indent=4, fp=file)
        file.truncate()

    exe_list = [y["name"] for x in new_execs for y in x]
    cleaned_names = sorted(set(new_names))
    cleaned_execs = sorted(set(exe_list))

    open('json/games.json','w').write(json.dumps(cleaned_names, indent=4))
    open('json/executables.json','w').write(json.dumps(cleaned_execs, indent=4))
