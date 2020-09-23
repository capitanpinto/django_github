from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests

from .models import *

def index(request):
    string = "string"
    code = request.GET.get('code', '')
    if(code):
        url = 'https://github.com/login/oauth/access_token'
        params = {
            'code':code,'client_id':'dbe43691bc3b0c94d2de','client_secret':'8b08f707f9f21a5552869627c3a55cfbc8d7c17b'
            }
        response = requests.post(url, data=params)
        if (hasattr(response, 'access_token')):
            objects = {"token": response.access_token}
        else:
            objects = {}
    else:
        objects = {}
    return render(request, 'github/index.html', objects)

def github_sign_in(request):
    try:
        new_question = Question(question_text=request.POST['question_text'], pub_date= timezone.now())
        new_question.save()
    except:
        return render('polls/new.html', {
            'error_message': "Something went wrong",
        })
    else:
        return HttpResponseRedirect(reverse('polls:detail', args=(new_question.id,)))
