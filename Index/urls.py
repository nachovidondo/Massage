from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views



urlpatterns = [
    path('',views.index, name='index'),
    path('contact/', views.contacto ,name ="contacto"),
    path('about-us/', views.about ,name ="about"),
    path('therapies/', views.therapies ,name ="therapies"),
    path('automatic/', views.automatic ,name="automatic"),
    path('therapist/', views.therapist, name="therapist")
]