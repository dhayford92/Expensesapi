from django.shortcuts import render
from .models import Source, Income
from .serializers import SourceSerializer, IncomeSerializer
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend



class SourceListView(generics.ListCreateAPIView):
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Source.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class SourceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SourceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Source.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)




class IncomeListView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['source']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Income.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)