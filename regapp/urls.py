from django.urls import path
from regapp.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('register/', reg, name='register'),
]
