from django.shortcuts import render

from .models import Usuarios
# Create your views here.
def index(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'index.html', {"usuarios" : Usuarios})