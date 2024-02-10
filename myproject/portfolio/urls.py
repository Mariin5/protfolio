from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path("photo_detail/<int:pk>/", views.photo_detail, name="photo_detail"),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
]