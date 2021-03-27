from django.shortcuts import render
from .models import Articles,Authors
from rest_framework import filters
from .serializers import SerialiserData, SerialiserMyData, serialiserauthor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class SearchAPIView(generics.ListCreateAPIView):
    search_fields = ['title']
    ordering_fields = ['contenttype', 'publicationdate']
    filterset_fields = {
        'publicationdate': ["gte", "lte"],
        'contenttype': ['exact'],
        'category': ['exact']
    }
    filter_backends = (filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter)
    queryset = Articles.objects.all()
    serializer_class = SerialiserMyData

# http://127.0.0.1:8000/api/?contenttype=Chapter%20ConferencePaper&search=python&publicationdate=2021-01-1


class details(generics.ListCreateAPIView):
    serializer_class = SerialiserData

    def get_queryset(self):
        queryset = Articles.objects.filter(pk=self.kwargs['post_id'])
        return queryset


class AuthorDetails(generics.ListCreateAPIView):
    serializer_class = serialiserauthor

    def get_queryset(self):
        queryset = Authors.objects.filter(pk=self.kwargs['author_id'])
        return queryset


class AuthorDetailsByName(generics.ListCreateAPIView):
    serializer_class = serialiserauthor

    def get_queryset(self):
        queryset = Authors.objects.filter(author_name=self.kwargs['author_name'])
        return queryset


# http://127.0.0.1:8000/api/details/50

