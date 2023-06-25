from flask import request

app = Flask(__name__)


@app.route('/', method="GET")
def handler_with_get_json(ff):
  r = request.json
  return r

@app.route('/', method="GET")
def handler_with_get_form(ff):
  r = request.form
  return r

@app.route('/', method="GET")
def handler_with_data(ff):
  r = request.data
  return r
