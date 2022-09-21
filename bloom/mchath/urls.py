from . import views
from django.urls import path

# class MyRegistrationView(RegistrationView):
#     def get_success_url(self,request, user):
#         return '/mchat/'

urlpatterns = [
    path('mchat/', views.mchat, name='mchat'),
    path('quizz/', views.quizz, name='quizz'),
    path('instruction/', views.instruction, name='instruction'),
    path('registerPage/', views.registerPage, name='registerPage'),
    path('next/', views.next),
    path('download_file_low/', views.download_file_low, name = 'download_file_low' ),
    path('download_file_mid/', views.download_file_mid, name = 'download_file_mid' ),
    path('download_file_hi/', views.download_file_hi, name = 'download_file_hi' ),


    # path('registerPage_post/', views.registerPage_post, name='registerPage_post'),
]
