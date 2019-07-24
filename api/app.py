#!/usr/bin/python

import falcon, bjoern
from falcon_cors import CORS
import endpoints.rooms as rooms
import endpoints.dorms as dorms
import endpoints.groups as groups
import endpoints.student as student
import endpoints.group_wishlist as group_wishlist
import endpoints.student_wishlist as student_wishlist
import session
from middleware.authentication import AuthenticationMiddleware

# TODO fix this
allowed_origins = ["*"]

cors = CORS(allow_origins_list=allowed_origins)
authentication = AuthenticationMiddleware()
api = falcon.API()

api = falcon.API(middleware=[cors.middleware, authentication])
# GET, DELETE, ###### DONE
api.add_route("/group", groups.Group())
api.add_route("/group/members", groups.GroupMembers())

# GET, DELETE, PUT
api.add_route("/group/invite", groups.GroupInvite())

# GET, PUT, DELETE ###### Done
api.add_route("/group_wishlist", group_wishlist.GroupWishlist())

# GET, PUT, DELETE ###### Done
api.add_route("/wishlist", student_wishlist.StudentWishlist())

# GET ###### DONE
api.add_route("/myinfo", student.MyInfo())

# GET ###### almost DONE
api.add_route("/dorms", dorms.Dorm())

# GET ###### almost DONE
api.add_route("/rooms", rooms.Room())

# for testing
session.create_session(0, "alex")
session.create_session(1, "denton")
session.create_session(2, "eli")
session.create_session(3, "michael")

try:
	bjoern.run(api, 'localhost', 8000)
except KeyboardInterrupt:
	pass
