import json
import sys

if __name__ == '__main__':
  with open(sys.argv[1], 'r') as fr:
    cont = json.load(fr)
    print('json.load(%s) # check passed' % (sys.argv[1]))
