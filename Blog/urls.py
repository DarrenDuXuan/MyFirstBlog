
from django.urls import path

from Blog import views

app_name = 'BlogList'

urlpatterns = [
    path('BlogList/', views.index, name='BlogList'),
]