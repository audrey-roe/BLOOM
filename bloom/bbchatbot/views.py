from email import message
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import redirect,render
from bbchatbot.mabi_main import get_response



# Create your views here.

def index_get(request):
    return render(request, 'basechat.html')

@csrf_exempt
def predict(request):
    # if request.method == 'POST':
        # text = request.get_json().get("message")
        data = json.loads(request.body)
        text = data['message']

        # text = request.POST.get('message')
        response = get_response(text)
        # data=response.json()
        # dump=json.dumps(data)
        message = {
            'answer':response
            }
        return JsonResponse(message)
        # data=response.json()
        # dump=json.dumps(data)
        # message = {
        #     'answer' : dump
        #     }
       
        # return render(request, message)

# def predict(request):
#     text = request.get_json().get("message")

#     response = get_response(text)
#     message = {"answer":response}
#     return jsonify(message)
