import glob
from pathlib import Path
import yaml
import os

for patches in glob.glob('_patch0/orbis/*.yml', recursive=True):
    app_titleid_str = 'app_titleid'
    with open(patches, 'r') as file:
      patch_file = yaml.safe_load(file)
      for doc in patch_file:
        for i in range(0, len(doc[app_titleid_str])):
          output = ("output/yml/{}.yml".format(doc[app_titleid_str][i]))
          with open(output, 'w') as fw:
            with open(patches, 'r') as file:
              content_ = file.read()
              content = ("##############################\n"
                         "# File generated from : {}\n"
                         "# DO NOT SUBMIT PULL REQUEST WITH THIS FILE!\n"
                         "# Submit original file instead.\n"
                         "##############################\n\n"
                         "{}".format(patches, content_))
              #print(content)
              fw.write(content)
