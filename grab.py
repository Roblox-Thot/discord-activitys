import http.client, json
Main:bool = True
PTB:bool = False
Canary:bool = False

#region Main discord
if Main:
    with open("json/detectable.json",'r+') as file:
        conn = http.client.HTTPSConnection("discord.com")

        conn.request("GET", "/api/v9/applications/detectable")

        res = conn.getresponse()
        data = res.read()

        old_data = json.load(file)
        new_data = json.loads(data.decode())

        old_names = [x['name'] for x in old_data]
        old_exes = [x['executables'] for x in old_data if "executables" in x]
        new_names = [x['name'] for x in new_data]
        new_exes = [x['executables'] for x in new_data if "executables" in x]
        
        # Print new names that are not in the old list
        added_games = [name for name in new_names if name not in old_names]
        added_execs = [name for name in new_exes if name not in old_exes]
        print("[Main]",f"{len(old_data)} -> {len(new_data)} games (+{len(new_data) - len(old_data)})")
        print("[Main] New games:",added_games)
        print("[Main] New executables:",len(added_execs))

        if len(added_games) or len(added_execs):
            file.seek(0)
            json.dump(new_data, indent=4, fp=file)
            file.truncate()
#endregion

#region PTB discord
if PTB:
    with open("json/ptb detectable.json",'r+') as file:
        conn = http.client.HTTPSConnection("ptb.discord.com")

        conn.request("GET", "/api/v9/applications/detectable")

        res = conn.getresponse()
        data = res.read()

        old_data = json.load(file)
        new_data = json.loads(data.decode())

        old_names = [x['name'] for x in old_data]
        old_exes = [x['executables'] for x in old_data if "executables" in x]
        new_names = [x['name'] for x in new_data]
        new_exes = [x['executables'] for x in new_data if "executables" in x]

        # Print new names that are not in the old list
        added_games = [name for name in new_names if name not in old_names]
        added_execs = [name for name in new_exes if name not in old_exes]
        print("[PTB]",f"{len(old_data)} -> {len(new_data)} games (+{len(new_data) - len(old_data)})")
        print("[PTB] New games:",added_games)
        print("[PTB] New executables:",len(added_execs))

        if len(added_games) or len(added_execs):
            file.seek(0)
            json.dump(new_data, indent=4, fp=file)
            file.truncate()
#endregion

#region Canary discord
if Canary:
    with open("json/canary detectable.json",'r+') as file:
        conn = http.client.HTTPSConnection("canary.discord.com")

        conn.request("GET", "/api/v9/applications/detectable")

        res = conn.getresponse()
        data = res.read()

        old_data = json.load(file)
        new_data = json.loads(data.decode())

        old_names = [x['name'] for x in old_data]
        old_exes = [x['executables'] for x in old_data if "executables" in x]
        new_names = [x['name'] for x in new_data]
        new_exes = [x['executables'] for x in new_data if "executables" in x]
        
        # Print new names that are not in the old list
        added_games = [name for name in new_names if name not in old_names]
        added_execs = [name for name in new_exes if name not in old_exes]
        print("[Canary]", f"{len(old_data)} -> {len(new_data)} games (+{len(new_data) - len(old_data)})")
        print("[Canary] New games:", added_games)
        print("[Canary] New executables:",len(added_execs))

        if len(added_games) or len(added_execs):
            file.seek(0)
            json.dump(new_data, indent=4, fp=file)
            file.truncate()
#endregion
