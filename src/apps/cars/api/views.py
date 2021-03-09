from rest_framework import generics
from apps.cars.models import Car
from apps.cars.api.serializers import CarSerializer

from functools import reduce
from operator import and_
from django.db.models import Q


class CarListView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()

        producer = self.request.query_params.get('producer')
        model = self.request.query_params.get('model')
        transmission = self.request.query_params.get('transmission')
        issue_year__gt = self.request.query_params.get('issue_year__gt')

        conditions = []

        if producer:
            conditions.append(Q(producer__icontains=producer))
        if model:
            conditions.append(Q(model__icontains=model))
        if transmission:
            conditions.append(Q(transmission=transmission))
        if issue_year__gt:
            conditions.append(Q(issue_year__gt=issue_year__gt))

        if conditions:
            queryset = queryset.filter(reduce(and_, conditions))
        
        return queryset


class CarRetrieveView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
