from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def post_list(request):
    return render(request, 'posts/post_list.html')

# Create your views here.
