from app2.views import dhoni
from django.urls import path
app_name='app2'
urlspatterns=[
    path('dhoni/',dhoni,name='dhoni')

]