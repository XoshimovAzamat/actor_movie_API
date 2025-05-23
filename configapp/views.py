from math import trunc

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.status import HTTP_200_OK
from .models import *
from rest_framework.views import APIView
from .serializers import ActorSerializer, MovieSerializer, CommitSerializer
from rest_framework.response import Response
from rest_framework import status


class ActorApi(APIView):
    def get(self, request):
        actors = Actors.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=400)


class MovieApi(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=400)


class CommitApiView(APIView):
    def get(self, request):
        response = {'success': True}
        commits = CommitMovie.objects.all()
        serializer = CommitSerializer(commits, many=True)
        response['data'] = serializer.data
        return Response(data=response)

    def post(self, request):
        response = {'success': True}
        serializer = CommitSerializer(data=request.data)
        user = request.user
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=user)
            response['data'] = serializer.data
            return Response(data=response)
        return Response(data=serializer.data)

