from django.http import Http404
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
from .models import Movie


class MoviesView(APIView):

    def get(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True, context={'request': request})
        return Response(serializer.data)

class MovieView(APIView):
    def get_object(self,request, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id):
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

