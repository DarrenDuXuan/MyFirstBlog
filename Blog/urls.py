
from django.urls import path

from Blog import views

app_name = 'BlogMainList'

urlpatterns = [
    path('BlogMainList/', views.blog_main_list, name='BlogMainList'),
    path('BlogDetail/<int:id>/', views.blog_detail, name='BlogDetail'),
    path('BlogCreate/', views.blog_create, name='BlogCreate')
]