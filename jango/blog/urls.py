from django.urls import path
from . import views

urlpatterns = [
    path('',views.Blog.as_view(), name = 'blog'),
    path('<int:id>',views.Post.as_view() , name='post')
]