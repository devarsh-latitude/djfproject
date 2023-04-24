from django.http import JsonResponse
import json

def api_home(request,*args,**kwargs):
    # print(dir(request))
    print(request.GET)
    body = request.body
    data={}
    try:
        data = json.loads(body)
    except:
        print("hii")

    data['params']=dict(request.GET)
    data['headers']=dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse({"message":"Hi there this is your Django API Response!"})