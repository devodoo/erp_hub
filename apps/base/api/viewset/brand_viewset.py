import requests
import json
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers.general_serializers import *
from ...models import EcommerceBrand
from rest_framework.decorators import action


class EcommerceBrandViewSet(viewsets.ModelViewSet):
    model = EcommerceBrand
    serializer_class = EcommerceBrandSerializer
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
                'message': 'Brand register successful.'
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
        user_serializer = EcommerceBrandSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Brand eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['put'])
    def update_brand_vtex(self, request, pk=None):
        for value in request.data['ids']:
            brand = self.get_object(value)
            platform = brand.platform
            url = platform.url + "/api/catalog/pvt/brand/" + str(brand.vtex_id)
            apikey = platform.api_key
            apitoken = platform.api_token
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-VTEX-API-AppKey": apikey,
            "X-VTEX-API-AppToken": apitoken
        }
        payload = {
            "Name": brand.name,
            "SiteTitle": brand.title,
            "Active": brand.active,
            "Text": brand.description,
        }
        try:
            response = requests.put(url, headers=headers, json=payload)
        except ConnectionError as error:
            return Response({
                'message': 'Error',
                'errors': response.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        if response.status_code == 200:
            brand.state = 'publish'
            brand.save()
            return Response({
                'message': 'Brand register successful in Vtex.',
                'state': 'publish'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Error',
                'errors': response.text
            }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def create_brand_vtex(self, request, pk=None):
        for value in request.data['ids']:
            brand = self.get_object(value)
            platform = brand.platform
            url = platform.url + "api/catalog/pvt/brand"
            apikey = platform.api_key
            apitoken = platform.api_token
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-VTEX-API-AppKey": apikey,
                "X-VTEX-API-AppToken": apitoken
            }
            payload = {
                "Name": brand.name,
                "SiteTitle": brand.title,
                "Active": brand.active,
                "Text": brand.description,
            }
            try:
                response = requests.post(url, headers=headers, json=payload)
            except ConnectionError as error:
                return Response({
                    'message': 'Error',
                    'errors': response.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            if response.status_code == 200:
                data_to_json = response.json()
                brand.vtex_id = data_to_json['Id']
                brand.state = 'publish'
                brand.save()
                return Response({
                    'message': 'Brand register successful in Vtex.'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)

    def search_platform(self, data):
        platform = EcommerceHub.objects.filter(
            Q(platfrom__iexact=data)
        ).first()
        return platform

    def search_brand(self, data):
        vtex_id = str(data.get('id'))
        brand = EcommerceBrand.objects.filter(
            Q(vtex_id__iexact=vtex_id)
        ).first()
        return brand

    @action(detail=False, methods=['post'])
    def get_brand_vtex(self, request, pk=None):
        for value in request.data['platform']:
            hub = self.search_platform(value)
            url = hub.url + "api/catalog_system/pvt/brand/list"
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
                    'message': 'No existe el hub que desea eliminar',
                    'error': error
                }, status=status.HTTP_404_NOT_FOUND)
            if response.status_code == 200:
                data_to_json = response.json()
                for data in data_to_json:
                    brand = self.search_brand(data)
                    if not brand:
                        payload = {
                            'name': data['name'],
                            'state': 'publish',
                            'platform': hub.id,
                            'vtex_id': data['id'],
                            'title': data['title'],
                            'active': data['isActive'],
                            'description': data['metaTagDescription'],
                        }
                        serializer_sale = self.serializer_class(data=payload)
                        if serializer_sale.is_valid():
                            serializer_sale.save()
                        else:
                            return Response({
                                'message': 'Error Bad Request',
                            }, status=status.HTTP_400_BAD_REQUEST)
                return Response({
                    'message': 'Marcas creadas correctamente'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)


