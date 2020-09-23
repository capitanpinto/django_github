from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('github_sign_in', views.github_sign_in, name='sign_in')
]