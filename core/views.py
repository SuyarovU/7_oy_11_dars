from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie
from rest_framework import status
from django.http import Http404


class HelloView(APIView):
    def get(self, request):
        return Response({'text':"Salom"})
    
    
class MovieView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        category = request.query_params.get('janr')
        nom = request.query_params.get('nom')
        yil = request.query_params.get('yil')
        rejissor = request.query_params.get('rejissor')
        if category:
            movies = Movie.objects.filter(janr__contains=category)
        elif nom:
            movies = Movie.objects.filter(nom__contains=nom)
        elif yil:
            movies = Movie.objects.filter(yil__contains=yil)
        elif rejissor:
            movies = Movie.objects.filter(rejissor__contains=rejissor)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class MovieDetailView(APIView):
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie not found!'})
        movie.delete()
        return Response({'status':'Movie deleted!'},status=status.HTTP_200_OK) 
    
    def put(self, request, pk):
        try:
            film = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie not found!'})
        serializer = MovieSerializer(film, data=request.data, partial=True) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



            