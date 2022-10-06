import json
import sys

with open(sys.argv[1], 'r') as fr:
  json.load(fr)
  print('json.load(%s) # check passed' % (sys.argv[1]))
