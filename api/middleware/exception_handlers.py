def InternalServerError(request, response, ex, params):
	raise falcon.HTTPError(falcon.HTTP_500)
