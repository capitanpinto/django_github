from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import requests
import json

from .models import *

def index(request):
    string = "string"
    code = request.GET.get('code', '')
    if(code):
        url = 'https://github.com/login/oauth/access_token'
        params = {'code':code,'client_id':'dbe43691bc3b0c94d2de','client_secret':'050c543622169581687d067b22a4e73a2f5d087b' }
        response = requests.post(url, data=params, headers={"Accept":"application/json"})
        objects = json.loads(response.content.decode('utf-8'))
        if ("access_token" in str(objects)):
            url = ' https://api.github.com/user/repos'
            access_token = objects['access_token']
            headers = {'Authorization':'token '+ access_token}
            response = requests.get(url, headers=headers)
            repositories = json.loads(response.content.decode('utf-8'))
            for repo in repositories:
               repo_exist = Repository.objects.filter(name=repo['name'], url=repo['svn_url']).count() > 0
               if (not repo_exist):
                   Repository(name=repo['name'], url=repo['svn_url']).save()
        else:
            objects = {'res': "something went wrong"}
    data = Repository.objects.all()
    return render(request, 'github/index.html', {'data':data})

def search_result(request):
    search_word = request.POST.get('search_word', '')
    data = Repository.objects.filter(name__contains=str(search_word))
    return render(request, 'github/search_result.html', {'data':data, 'search_word': search_word})

def search(request):
        search_word = request.GET.get('search_word', '') 
        print(search_word)
        print("jessica")
        return HttpResponseRedirect(reverse('github:search_result'))