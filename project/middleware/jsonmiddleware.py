import json

class JSONMiddleware:
    def process_request(self, request):
        if request.content_type == 'application/json':
            request.JSON = json.loads(request.body.decode('utf-8'))
        return None



