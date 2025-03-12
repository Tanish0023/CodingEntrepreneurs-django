import json
from django.http import JsonResponse

def api_home(request):

    body = request.body
    data = {}

    try:
        data = json.loads(body)
    except:
        pass

    print(data.keys())
    print(request.headers)
    return JsonResponse({"message": "Hi there"})