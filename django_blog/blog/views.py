from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello Django")

def today_is(request):
    return render(request, 'blog/datetime.html', { 'now': datetime.datetime.now() })