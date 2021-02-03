from collections import namedtuple
import json

class Product:
  def __init__(self, productid=None, productname=None, 
              onlineflag=None, onlinefrom=None, availableflag=None,
              brand=None, color=None, category=None, seasonyear=None,
              shortdescription=None, size=None,  *args, **kwargs):
    self.productid = productid
    self.productname = productname
    self.onlineflag = onlineflag
    self.onlinefrom = onlinefrom
    self.availableflag = availableflag
    self.brand = brand
    self.color = color
    self.category = category
    self.seasonyear = seasonyear
    self.shortdescription = shortdescription
    self.size = size
  
  def toJSON(self):
      return json.dumps(self, default=lambda o: o.__dict__, 
          sort_keys=True, indent=4)