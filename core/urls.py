from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieView.as_view()),
    path('movies/<int:pk>', views.MovieDetailView.as_view()),
    path('hello/', views.HelloView.as_view())
]
