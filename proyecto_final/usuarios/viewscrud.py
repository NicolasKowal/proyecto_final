from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User

class User_List(ListView):
    model = User 
    template_name = "usuarios/crud_user_list.html"

class User_Detail(DetailView):
    model = User
    template_name = "usuarios/crud_user_detalle.html"

class User_View(CreateView):
    ...
    # model = User
    # success_url = reverse_lazy('List')
    # fields = [' ', ' ']

class User_Update(UpdateView):
    model = User
    success_url = reverse_lazy('List')
    template_name = 'usuarios/crud_user_form.html'
    fields = ['first_name', 'last_name', 'password', 'email']

class User_Delete(DeleteView):
    model = User
    template_name = 'usuarios/crud_user_delete.html'
    success_url = reverse_lazy('List')