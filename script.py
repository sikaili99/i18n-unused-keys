import os
import re
import json


# Get keys from the e-us.json file
with open('keys.json', 'r') as json_file:
    list_data = json.load(json_file)
    with open('new-keys.txt', 'w') as file:
        for line in list(list_data.keys()):
            file.write(line)
            file.write('\n')


# Get used keys from javaScript files
with open("data.txt") as words:
    flat_list=[word for line in words for word in line.split()]
    rx = re.compile('|'.join(flat_list))
    found_data = []
    for root, dirs, files in os.walk('src/componets'):
        for filename in files:
            with open('src/componets/'+filename, 'rb') as df:
                data = df.read().decode('utf-8')
            for match in rx.finditer(data):
                # Use the MatchObject as you like
                if match.group() not in found_data:
                    # Use set for faster
                    found_data.append(match.group())

    # Save used keys to keys.txt
    with open('keys.txt', 'w') as f:
        for line in found_data:
            f.write(line)
            f.write('\n')

# Can be a json file, openand read it!
eus_json = {
    "common.edit": {
        "text":"Love",
        "note": ""
    },
    "love.test":{
        "text":"Love",
        "note": ""
    },
    "common.love.get":{
        "text":"Love",
        "note": ""
    },
    "common.lo.get":{
        "text":"Love",
        "note": ""
    },
    "common.ve.get":{
        "text":"Love",
        "note": ""
    },
    "you.i": {
        "text":"Love",
        "note": ""
    },
    "common.e.get":{
        "text":"Love",
        "note": ""
    }
}

# Check the key is not used and delete it.
def delete_unused_keys():
    with open('keys.json', 'r') as json_file:
        list_data = json.load(json_file)
    with open('keys.txt', 'r') as file_keys:
        used = [key.rstrip() for key in file_keys]
        print("used keys", used)
        for key in list_data: 
            if key not in used:
                del eus_json[str(key.strip())]
        # Save to new json file
        print(eus_json)               

delete_unused_keys()
