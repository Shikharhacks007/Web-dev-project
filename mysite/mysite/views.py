from django.shortcuts import render
import os
import urllib.request
import sys
import webbrowser

# Create your views here.
def welcome(request):
    return render(request,'homepage.html')

def chat(request):
    return render(request, 'chat.html')


