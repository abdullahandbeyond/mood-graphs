from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.create_view, name='add_mood'),
    path('filter_mood/', views.filter_mood, name='filter_mood')
]
