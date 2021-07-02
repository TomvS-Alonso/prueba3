from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'base/principal.html')

def contacto(request):
    return render(request, 'base/contacto.html')