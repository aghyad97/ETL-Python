from flask import Flask, render_template, Response
from utils.to_json import xml_to_json, csv_to_json
import config
import traceback
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  """ This route for index and renders index.html .
  """
  return render_template('index.html')

@app.route('/json/<filename>', methods=['GET'])
def getJsonFile(filename):
  """ This route for /json and takes parameter.
  which is the filename and send back the
  in json format.
  """
  try:
    if str(filename).endswith('1'):
      data = xml_to_json()
      return Response(data, 
                      status=200, 
                      headers={"Content-Disposition":
                      "attachment;filename=" + filename + ".json"},
                      mimetype='application/json')
    elif str(filename).endswith('2'):
      data = csv_to_json()
      return Response(data, 
                      status=200, 
                      headers={"Content-Disposition":
                      "attachment;filename=" + filename + ".json"},
                      mimetype='application/json')
    raise Exception("File not found")
  except Exception as e:
    logging.error(traceback.format_exc())
    

@app.errorhandler(404)
def page_not_found(e):
    """ Handling Undefined routes. """
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)