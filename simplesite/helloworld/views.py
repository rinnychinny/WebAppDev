from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    response_string = Hello.objects.all()[0]
    return render(request, 'helloworld/index.html', {'data': response_string})
# Create your views here.

def simple_view(request):
    header = request.META
    ip = header['REMOTE_ADDR']
    html = "<html><head></head><body>Your ip address is: "+ip+"</body></html>"
    return HttpResponse(html, content_type="text/html", status=200)