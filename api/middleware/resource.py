from utils import get_session
import session

class ResourceMiddleware(object):
	def process_resource(self, request, response, resource, params):
		resource.session_token = get_session(request)
		resource.student_id = session.id_from_session(resource.session_token)
