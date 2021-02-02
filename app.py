from flask import Flask, request, render_template, json, make_response
import config
from utils import xml_to_json, csv_to_json
from models import Product

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  """
  This route for index and renders index.html .
  """
  return render_template('index.html')

@app.route('/json/<filename>', methods=['GET'])
def getJsonFile(filename):
  """
  This route for /json and takes parameter.
  which is the filename and send back the
  in json format.
  """
  if str(filename).endswith('.xml'):
    data = xml_to_json()
    response = app.response_class(
        response= data,
        status=200,
        mimetype='application/json'
    )
    return response
  elif str(filename).endswith('.csv'):
    data = csv_to_json()
    response = app.response_class(
        response=data, #json.dumps(data)
        status=200,
        mimetype='application/json'
    )
    return response
  response = app.response_class(
      response= 'bad request!',
      status= 404,
      mimetype='application/json'
  )
  return response

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)