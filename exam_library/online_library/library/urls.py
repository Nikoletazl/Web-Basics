from django.urls import path

from online_library.library.views import home, add_book, edit_book, details_book, show_profile, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = [
    path('', home, name='home'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('details/<int:pk>/', details_book, name='details book'),

    path('profile/create/', create_profile, name='create profile'),
    path('profile/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]