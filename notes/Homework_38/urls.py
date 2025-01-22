from django.urls import path
from notes.Homework_38.views import hello_notes

urlpatterns =  [
    path('', hello_notes, name='hello_notes'),
]