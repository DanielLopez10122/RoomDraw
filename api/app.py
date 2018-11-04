#!/usr/bin/python

import falcon, bjoern

api = falcon.API()

bjoern.run(api, 'localhost', 8000)
