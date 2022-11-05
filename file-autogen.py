import glob
from pathlib import Path
import yaml
import os
import json

if __name__ == '__main__':
  for patches in glob.glob('_patch0/orbis_new/*.json', recursive=True):
    app_titleid_str = 'app_titleid'
    with open(patches, 'r') as file:
      patch_file = json.load(file)
      json_id = patch_file["patch"]
      for i in range(0, len(json_id[0][app_titleid_str])):
        out = ('output/json/{}.json'.format(json_id[0][app_titleid_str][i]))
        with open(out, 'w') as fw:
          with open(patches, 'r') as fr:
            fw.write(fr.read())
