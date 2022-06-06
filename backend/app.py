import os
from flask import Flask, send_from_directory
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

swagger_template = dict(
    info={'title': 'My first Swagger UI document',
          'version': '0.1',
          'description': 'This document depicts a  Sleuth Swagger UI' },
    )

swagger_config = {"headers": [],
                  "specs": [{
                      "endpoint": 'hello-world',
                      "route": '/hello_world',
                      "rule_filter": lambda rule: True,
                      "model_filter": lambda tag: True,
                  }],
                  "static_url_path": "/flasgger_static",
                  "swagger_ui": True,
                  "specs_route": "/apidocs/"}


app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
swagger = Swagger(app, template=swagger_template, config=swagger_config)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

@swag_from("hello_world.yml", methods=['GET'])
@app.route("/")
def hello_world():
    return "Hello World!!!"

def import_by_reflection(name):
    components = name.split('.')
    mod = __import__(components[0])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

@app.route("/hello")
def hello():
    class_name = os.environ.get('suffix_class', 'backend.suffix.World')
    cls = import_by_reflection(class_name)
    obj = cls()
    return "Hello " + obj.get_suffix()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)