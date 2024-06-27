from django.urls import path
from .import views


app_name ='voyage_admin'


urlpatterns = [
   path('', views.acceuil, name='acceuil'),
  

   

]