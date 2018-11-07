#!/usr/bin/python

import falcon, bjoern
import endpoints.groups as groups

api = falcon.API()

api.add_route("/GetGroup", groups.Group())

bjoern.run(api, 'localhost', 8000)
