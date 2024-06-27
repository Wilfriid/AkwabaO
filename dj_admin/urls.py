from django.contrib import admin
from django.urls import path , include


from voyage_admin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('voyage_admin/', include('voyage_admin.urls')),
    path('destination/', views.destination, name='destination'),  
    path('abidjan/', views.abidjan, name='abidjan'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('offres/', views.offres, name='offres'),
    path('contact/', views.contact, name='contact'),
    path('propos/', views.propos, name='propos'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('statistique/', views.statistique, name='statistique'),

   
    
    
]
