# Create your views here.
import re
from django.http import Http404
from django.shortcuts import redirect,render
from django.core.paginator import Paginator
# from django.contrib.auth import login,logout,authenticate
# from .forms import createcustomerform, quizform
from .models import quiz, customer
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger


# Create your views here.

# def registerPage(request):
#     if request.POST:
#         form = createcustomerform(request.POST, request.FILES)
#         print = (request.FILES)
#         if form.is_valid():
#           form.save()
#         else :
#             raise Http404
#         # return redirect(quizz)
#     context = {'form': form}
#     return render(request, 'signinfo.html', context)
def registerPage(request):
    if request.method == 'POST':     
        if customer.objects.filter(caregiver_email='caregiver_email').exists():
            return redirect (quizz)
        else:
            customer.objects.create(
                    caregiver_name = request.POST['caregiver_name'],
                    child_age = request.POST['child_age'].replace(' Months',''),
                    child_name = request.POST['child_name'],
                    caregiver_email = request.POST['caregiver_email'],
                    relation_to_child=request.POST['relation_to_child'],
                    caregiver_phone = int(f"234{(request.POST['phone'].replace('+','')).replace('234234','').replace('234','')}"),
                    date = request.POST['date'],)

        return redirect(quizz)
    else:
        return render (request, 'info-form-page.html')
    # return redirect(quizz)

def mchat(request):
    return render(request, 'mchat-intro-page.html')

def instruction(request):
    return render(request, 'mchat-instructions-page.html')

def quizz(request):
    if request.method == 'POST':
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
            if q.ans ==  request.POST.get(q.question):
                score+=1
                correct+=1
            # else:
            #     wrong+=1
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