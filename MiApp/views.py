from django.shortcuts import render

# Create your views here.
def genindex(request): 
    return render(request, 'index.html')
def gentest(request):
    return render(request, 'test.html')