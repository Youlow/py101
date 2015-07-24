# -*- coding: utf-8 -*-
"""
    Doc ...
    ...

    :How to:
    To start dev web server use:
        sudo gunicorn -b 0.0.0.0:80 api:app

"""
from __future__ import unicode_literals, print_function

import json

import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class Index:
    def on_get(self, req, resp):
        """ Handle GET request
        :param req:
        :param resp:
        :return:
        """
        resp.status = falcon.HTTP_200
        resp.body = (json.dumps({
            'some_int': 42,
            'some_dict': {
                'My reach': 'is global',
                'My tower': 'secure',
                'My couse': 'is noble',
                'My power': 'is pure',
            },
            'key': 'value'
        }))

    def on_post(self, req, resp, user_name):
        pass


app = falcon.API()

index = Index()

app.add_route('/', index)
