from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def hola(request): 
    return render(request, 'index.html')
@login_required
def hola2(request):
    return render(request, 'restringir.html')