from app1.views import virat
from django.urls import path
app_name='app1'
urlspatterns=[
    path('virat/',virat,name='virat')

]
