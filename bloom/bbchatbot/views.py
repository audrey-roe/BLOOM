import json
import requests
from django.shortcuts import redirect,render
from mabi_main import get_response



# Create your views here.

def index():
    # return (base.html)
    pass

def predict(request):
    if request.method == 'POST':
        text = request.POST.get('message')
        response = get_response()
        data=response.json()
        dump=json.dumps(data)
        message = {
            'answer' : response
            }
       
        return render  (request, 'basechat.html', message)
