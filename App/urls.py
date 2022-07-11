from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [    
    path('' , views.inicio, name="Inicio"),
    path('datos/', views.datos,name="Datos"),
    path('login',views.login_request, name='login'),
    path('register',views.register, name = 'Register'),
    path('logout',LogoutView.as_view(template_name='App/logout.html'), name = 'Logout'),
    path('datos/list', views.DatosList.as_view(), name='list'),
    path(r'^(?P<pk>\d+)$' , views.DatosDetalle.as_view(), name='Detail'),
    path(r'^nuevo$',views.DatosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.DatosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.DatosDelete.as_view(), name='Delete'),
    path('editarPerfil' , views.editarPerfil, name='EditarPerfil'),
    

]    