import requests
from django.db.models import Q
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers.general_serializers import *
from ...models import EcommerceWarehouse
from rest_framework.decorators import action


class EcommerceWarehouseViewSet(viewsets.ModelViewSet):
    model = EcommerceWarehouse
    serializer_class = EcommerceWarehouseSerializer
    queryset = None
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects \
                .filter(is_active=True)
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Warehouse register successful.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = EcommerceWarehouseSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Warehouse actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Warehouse eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)

    def search_platform(self, data):
        platform = EcommerceHub.objects.filter(
            Q(platfrom__iexact=data)
        ).first()
        return platform

    @action(detail=False, methods=['post'])
    def get_warehouse_vtex(self, request):
        for value in request.data['platform']:
            hub = self.search_platform(value)
            url = hub.url + "/api/logistics/pvt/configuration/warehouses"
            apikey = hub.api_key
            apitoken = hub.api_token
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-VTEX-API-AppKey": apikey,
                "X-VTEX-API-AppToken": apitoken
            }
            try:
                response = requests.get(url, headers=headers)
            except ConnectionError as error:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)

            if response.status_code == 200:
                data_to_json = response.json()
                for data in data_to_json:
                    warehouse_id = EcommerceWarehouse.objects.filter(
                        Q(vtex_id__iexact=str(data['id']))
                    ).first()
                    if not warehouse_id:
                        vals = {
                            'name': data['name'],
                            'code': data['id'],
                            'vtex_id': data['id'],
                            'platform': hub.id,
                        }
                        serializer_warehouse = self.serializer_class(data=vals)
                        if serializer_warehouse.is_valid():
                            serializer_warehouse.save()
                return Response({
                    'message': 'Warehouse was created successful!'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)



