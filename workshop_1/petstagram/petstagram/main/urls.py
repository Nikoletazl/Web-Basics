from django.urls import path

from petstagram.main.views import show_home, show_dashboard, show_profile, show_pet_photo_details

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet photo details'),
)