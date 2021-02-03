import os
import json
import csv
from models import Product
import traceback
import logging

list = []

def csv_to_json():
  try:
    with open('data/brand2.csv', 'r') as f:
      reader = csv.DictReader(f)
      next(reader)
      for row in reader:
        j = json.loads(json.dumps(dict(row)))
        product = Product(**j)
        list.append(product.toJSON())
    return list
  except Exception as e:
    logging.error(traceback.format_exc())



def xml_to_json():
  try:
    return
  except Exception as e:
    logging.error(traceback.format_exc())