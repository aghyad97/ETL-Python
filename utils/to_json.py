from models import Product
import xml.etree.ElementTree as ET
import json
import csv
import traceback
import logging

"""
This method takes the csv file and read it as
dict row by row, create Product object with
the info, then append json format of the product
to the master list (list)
"""
def csv_to_json():
  list = []
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

"""
This method takes the xml file and iterate through
it, checks for specific attributes and tag, create
Product object with the info, then append json
format of the product to the master list (list)
"""
def xml_to_json():
  list = []
  try:
    tree = ET.parse('data/brand1.xml')
    root = tree.getroot()
    for product in root:
      productJson = {}
      size = []
      for item in product.iter():
        if item.attrib.get('attribute-id') == 'Season':
          """ Season attribute. """
          productJson['seasonyear'] = item.text
        elif item.attrib.get('attribute-id') == 'Category':
          """ Category attribute. """
          productJson['category'] = item.text
        elif item.tag == 'display-value':
          """ Size attribute. """
          size.append(item.text)
        else: 
          if len(item) == 0 and item.text != 'size':
            productJson[item.tag] = item.text
      productJson['size'] = size
      size = []
      js = json.loads(json.dumps(dict(productJson)))
      product = Product(**js)
      list.append(product.toJSON())
    return list
  except Exception as e:
    logging.error(traceback.format_exc())