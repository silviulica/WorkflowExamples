import json
import time
import sys

def generate_data(outfile, size):
  with open(outfile, 'wt') as f:  
    for _ in xrange(size):
      for ix in xrange(100):
        f.write('%s\n' % json.dumps(
            {'ProductID': 1 + ix, 'ProductName': 'Product(%s)' % ix, 'Price': ix * 10, 'Timestamp': time.time()}))

generate_data(sys.argv[1], 1000)
