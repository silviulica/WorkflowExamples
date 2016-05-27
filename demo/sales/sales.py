import json

class Product(object):
  def __init__(self, name, id):
    self.name = name
    self.id = id

def parse_record(e):
    r = json.loads(e)
    return Product(r['ProductName'], r['ProductID']), r['Price']


