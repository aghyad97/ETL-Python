from models import Product
import xml.etree.ElementTree as ET
import json
import csv
import traceback
import logging

list = []

def csv_to_json():
  try:
    with open('data/brand2.csv', 'r') as f:
      reader = csv.DictReader(f)
      next(reader)
      for row in reader:
        print(type(row))
        break
        j = json.loads(json.dumps(dict(row)))
        product = Product(**j)
        list.append(product.toJSON())
    return list
  except Exception as e:
    logging.error(traceback.format_exc())


def xml_to_json():
  try:
    tree = ET.parse('data/brand1.xml')
    root = tree.getroot()
    for product in root:
      j = {}
      size = []
      for item in product.iter():
        if item.attrib.get('attribute-id') == 'Season':
          """ Season attribute. """
          j['seasonyear'] = item.text
        elif item.attrib.get('attribute-id') == 'Category':
          """ Category attribute. """
          j['category'] = item.text
        elif item.tag == 'display-value':
          """ Size attribute. """
          size.append(item.text)
        else: 
          if len(item) == 0 and item.text != 'size':
            j[item.tag] = item.text
      j['size'] = size
      size = []
      js = json.loads(json.dumps(dict(j)))
      product = Product(**js)
      list.append(product.toJSON())
    return list
  except Exception as e:
    logging.error(traceback.format_exc())