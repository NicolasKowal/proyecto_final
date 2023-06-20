from django.urls import path, include
from usuarios import views, viewscrud
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='usuarios/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    
    
    path('', views.index, name= 'index')
]

urlpatterns += [
    path('d', viewscrud.User_List.as_view(), name='List'),
    path('<int:pk>', viewscrud.User_Detail.as_view(), name='Detail'),
    path('nuevo', viewscrud.User_View.as_view(), name='New'),
    path('editar/<int:pk>', viewscrud.User_Update.as_view(), name='Edit'),
    path('borrar/<int:pk>', viewscrud.User_Delete.as_view(), name='Delete'),
]
