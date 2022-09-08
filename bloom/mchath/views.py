# Create your views here.
import os 
from django.shortcuts import redirect,render
from django.core.paginator import Paginator
# from django.contrib.auth import login,logout,authenticate
# from .forms import createcustomerform, quizform
from .models import quiz, customer
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from .utils import render_to_pdf



# Create your views here.

# def registerPage(request):
#     if request.method == 'POST':     
#         if customer.objects.filter(caregiver_email='caregiver_email').exists():
#             return redirect (quizz)
#         else:
#             customer.objects.create(
#                     caregiver_name = request.POST['caregiver_name'],
#                     child_age = request.POST['child_age'].replace(' Months',''),
#                     child_name = request.POST['child_name'],
#                     caregiver_email = request.POST['caregiver_email'],
#                     relation_to_child=request.POST['relation_to_child'],
#                     caregiver_phone = int(f"234{(request.POST['phone'].replace('+','')).replace('234234','').replace('234','')}"),
#                     date = request.POST['date'],)

#         return redirect(quizz)
#     else:
#         return render (request, 'info-form-page.html')
    # return redirect(quizz)

def registerPage(request):
    if request.method == 'POST':     
        # if not customer.objects.filter(caregiver_email = request.POST.get['caregiver_email']).exists():
            # return redirect (quizz)
            customer.objects.create(
                    caregiver_name = request.POST['caregiver_name'],
                    child_age = request.POST['child_age'].replace(' Months',''),
                    child_name = request.POST['child_name'],
                    caregiver_email = request.POST['caregiver_email'],
                    caregiver_phone = int(f"234{(request.POST['phone'].replace('+','')).replace('234234','').replace('234','')}"),
                    date = request.POST['date1'],)

            return render(request, 'mchat-survey-page.html')
            # return redirect(quizz)
    else:
        return render(request, 'info-form-page.html')

def mchat(request):
    return render(request, 'mchat-intro-page.html')

def instruction(request):
    return render(request, 'mchat-instructions-page.html')

def quizz(request):
    if request.method == 'POST':
        for questions in request.POST:
            request.session[questions] = request.POST[questions]

        print(request.POST)


        questions=quiz.objects.all()
        score = 0
        # wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.session.get(q.question):
                score+=1
                correct+=1
        context = {
            'total':total,
            'score': score
        }
        print(context)
        return render(request, 'mchat-results-page.html', context)
    else:
        questions=quiz.objects.all()

    p = Paginator(questions, 4) # 4 questions per page this determines how many objects will be displayed per page
    page_num = request.GET.get('page', 1) # allows you to access pages by passing value directly  through link
    page = p.page(page_num)

    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page = Paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page = p.page(1)
    
    
    context = { 
        'questions':page 
    
        # 'questions':questions
    }
    
    return render(request, 'mchat-survey-page.html', context)

def result(request):
    return render(request, 'mchat-results-page.html', )


def next(request):
    if request.method == 'POST':
        for questions in request.POST:
            request.session[questions] = request.POST[questions]
        hun = request.POST['next_link']
        return redirect(f'/quizz?page={hun}')


# def resultpdf(request):
#     #Retrieve data or whatever you need
#     return render_to_pdf(
#             'mchat-results-page.html',
#             {
#                 'pagesize':'A4',
#                 'mylist': results,
#             }
#         )

# from django.shortcuts import render
# from django.http import HttpResponse
# from wsgiref.util import FileWrapper


# def download_pdf(request):
#     filename = 'faults.pdf'
#     content = FileWrapper(filename)
#     response = HttpResponse(content, content_type='application/pdf')
#     response['Content-Length'] = os.path.getsize(filename)
#     response['Content-Disposition'] = 'attachment; filename=%s' % 'faults.pdf'
#     return response

import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse
# Import render module
from django.shortcuts import render
from pathlib import Path
import pandas as pd


def download_file_low(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_name = 'low_risk_result.pdf'
    filepath = BASE_DIR + '/mchath/Files/' + file_name
    file = open(filepath.format(file_name), 'rb')
    response = HttpResponse(file, content_type='application/pdf')
    response['Content-Disposition'] = "attachment; filename={}".format(file_name)
    return response