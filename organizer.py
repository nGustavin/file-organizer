import json
import os
import shutil


def organizer(user: str, typesDir):
  downloadsPath = f'/home/{user}/Downloads'
  files = os.listdir(downloadsPath)
  
  with open(typesDir) as types:
    types = json.load(types)
    os.chdir(downloadsPath)
    for type in types:
      try:
        os.makedirs(downloadsPath + '/' + type['name'])
      except:
        print(f'Directory {type["name"]} already exists')
      for ext in type['extensions']:
        for file in files:
          if(file.endswith(ext)):
            shutil.move(file, type['name'])
