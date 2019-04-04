#!/usr/bin/python

import falcon, bjoern
import endpoints.rooms as rooms
import endpoints.dorms as dorms
import endpoints.groups as groups
import endpoints.myinfo as myinfo
import endpoints.group_wishlist as group_wishlist
import endpoints.student_wishlist as student_wishlist
import session

api = falcon.API()

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
api.add_route("/myinfo", myinfo.MyInfo())

# GET ###### almost DONE
api.add_route("/dorms", dorms.Dorm())

# GET ###### almost DONE
api.add_route("/rooms", rooms.Room())

# for testing
session.create_session(2, "alex")
session.create_session(1, "denton")

try:
	bjoern.run(api, 'localhost', 8000)
except KeyboardInterrupt:
	pass
