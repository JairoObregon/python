from django.shortcuts import render
from django.urls import reverse
#
import datetime
from .models import servicio,usuario   
from .serializers import UsuarioSerializer
from rest_framework import viewsets

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.detail import DetailView



# Create your views here.

def time(request):
    x = datetime.datetime.now()
    return render( request,'core/home.html', context={ 'data' : x.strftime('%d-%m-%Y')})

def nosotros(request):
    return render( request,'core/nosotros.html')

def servicios(request):
    x = servicio.objects.all()
    return render( request,'core/servicio.html', context={ 'data' : x})

#ccbv
#listar
class UserListView(ListView):
    model = usuario

#crear
class UserCreate(CreateView):
    model = usuario
    fields = ['Nombres','Apaterno','Amaterno','Edad']

    def get_success_url(self):
        return reverse('list')


#eliminar
class UserDelete(DeleteView):
    model = usuario
    success_url = reverse_lazy('list')

#actualizar
class UserUpdate(UpdateView):
    model = usuario
    fields = ['Nombres','Apaterno','Amaterno','Edad']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('list')

#detail
class UserDetailView(DetailView):
    model = usuario
    


#django rest framework
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = UsuarioSerializer




