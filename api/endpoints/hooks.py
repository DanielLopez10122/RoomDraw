import session
from utils import *

def on_request(request, response, resource, params):
	resource.session_token = request.headers.get("SESSION-ID")
	resource.student_id = session.id_from_session(resource.session_token)
