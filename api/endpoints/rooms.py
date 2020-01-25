#!/usr/bin/python

import falcon
from private import *
import models

from utils import *

class Room(object):
	def on_get(self, request, response):
		room_number = INT(request.params.get("room_number"))
		spots_left =  INT(request.params.get("spots_left"))
		floor =       INT(request.params.get("floor"))
		dorm_id =     INT(request.params.get("dorm_id"))

		sql = sql_create_session()
		response.media = sql.query(models.Room).filter_by(dorm_id_id=dorm_id, room_number=room_number, available_spots=spots_left, floor=floor).first().dict()
