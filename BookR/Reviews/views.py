from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    name = request.GET.get('name', '')
    return render(request, "base.html", {"name": name})