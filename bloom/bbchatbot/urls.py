from . import views
from django.urls import path

urlpatterns = [
        path('', views.index_get, name='inget'),
        path('predict', views.predict, name='predict'),

]