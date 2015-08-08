# -*- coding: utf-8 -*-
"""
    Flask: http://flask.pocoo.org/docs/0.10/quickstart/
    Flask-API: https://flask-restful.readthedocs.org/en/0.3.4/quickstart.html

    :HowTo:
    To run dev server:
    ``` (env)➜  py101 git:(web-view) ✗ sudo python ex1/www/web_app.py ```
    * To run server on :80 port you should use sudo

    :Note:
    Server will restart automatically, when you change this file.
    * very useful for debugging
"""
from flask import Flask, render_template
from flask.ext.restful import Api, Resource, reqparse

__author__ = 'egregors'

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# TODO: add your args
parser.add_argument('state')
# parser.add_argument('agr1')
# parser.add_argument('agr2')


# Flask routes. Nothing to do this.
@app.route("/")
def index():
    """ Main HTTP view.
    :return: resp template with func js.
    """
    return render_template('index.html')


# API entries. All API logic should be there.
class GetStatus(Resource):
    def get(self):
        """ GET method example
        :return: json
        """
        return {'status': 'OK'}

    def post(self):
        """ POST method example
        :return: None
        """
        args = parser.parse_args()
        print(args['state'])


api.add_resource(GetStatus, '/api/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
