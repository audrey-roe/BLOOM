from . import views
from django.urls import path

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/mchat/'

urlpatterns = [
    path('', views.mchat, name='mchat'),
    path('quizz/', views.quizz, name='quizz'),
    # path('quizzz/', views.quizzz, name='quizz'),

    path('instruction/', views.instruction, name='instruction'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('next/', views.next)

    # path('registerPage_post/', views.registerPage_post, name='registerPage_post'),
]