import requests
from django.db.models import Q
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers.general_serializers import *
from ...models import EcommerceCategory
from rest_framework.decorators import action


class EcommerceCategoryViewSet(viewsets.ModelViewSet):
    model = EcommerceCategory
    serializer_class = EcommerceCategorySerializer
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
                'message': 'Category register successful.'
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
        user_serializer = EcommerceCategorySerializer(user, data=request.data)
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
                'message': 'Category eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'])
    def create_category_vtex(self, request, pk=None):
        for value in request.data['ids']:
            category = self.get_object(value)
            platform = category.platform
            url = platform.url + "api/catalog/pvt/category"
            apikey = platform.api_key
            apitoken = platform.api_token
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-VTEX-API-AppKey": apikey,
                "X-VTEX-API-AppToken": apitoken
            }
            payload = {
                "Name": category.name if category.name else '',
                "FatherCategoryId": category.parent.vtex_id if category.parent else '',
                "Title": category.title if category.title else '',
                "Description": category.description if category.description else '',
                "Keywords": category.keywords if category.keywords else '',
                "IsActive": category.active,
                "LomadeeCampaignCode": category.remarketing_code if category.remarketing_code else '',
                "AdWordsRemarketingCode": category.remarketing_code if category.remarketing_code else '',
                "ShowInStoreFront": category.showing_storefront,
                "ShowBrandFilter": category.show_brand_filter,
                "ActiveStoreFrontLink": category.store_front_link,
                "StockKeepingUnitSelectionMode": category.mtto if category.mtto else '',
                "Score": category.score,
                "GlobalCategoryId": category.global_category if category.global_category else '',
            }
            try:
                response = requests.post(url, headers=headers, json=payload)
            except ConnectionError as error:
                return Response({
                    'message': 'Error',
                    'errors': error
                }, status=status.HTTP_400_BAD_REQUEST)
            if response.status_code == 200:
                data_to_json = response.json()
                category.vtex_id = data_to_json['Id']
                category.state = 'publish'
                category.save()
                return Response({
                    'message': 'Brand register successful in Vtex.',
                    'state': 'publish'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def update_category_vtex(self, request, pk=None):
        for value in request.data['ids']:
            category = self.get_object(value)
            platform = category.platform
            url = platform.url + "api/catalog/pvt/category"+str(category.vtex_id)
            apikey = platform.api_key
            apitoken = platform.api_token
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-VTEX-API-AppKey": apikey,
                "X-VTEX-API-AppToken": apitoken
            }
            payload = {
                "Name": category.name if category.name else '',
                "FatherCategoryId": category.parent.vtex_id if category.parent else '',
                "Title": category.title if category.title else '',
                "Description": category.description if category.description else '',
                "Keywords": category.keywords if category.keywords else '',
                "IsActive": category.active,
                "LomadeeCampaignCode": category.remarketing_code if category.remarketing_code else '',
                "AdWordsRemarketingCode": category.remarketing_code if category.remarketing_code else '',
                "ShowInStoreFront": category.showing_storefront,
                "ShowBrandFilter": category.show_brand_filter,
                "ActiveStoreFrontLink": category.store_front_link,
                "StockKeepingUnitSelectionMode": category.mtto if category.mtto else '',
                "Score": category.score,
                "GlobalCategoryId": category.global_category if category.global_category else '',
            }
            try:
                response = requests.put(url, headers=headers, json=payload)
            except ConnectionError as error:
                return Response({
                    'message': 'Error',
                    'errors': error
                }, status=status.HTTP_400_BAD_REQUEST)
            if response.status_code == 200:
                category.state = 'publish'
                category.save()
                return Response({
                    'message': 'Brand register successful in Vtex.',
                    'state': 'publish'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)

    def get_category_info(self, url, apikey, apitoken, category):
        url_complete = url + "api/catalog/pvt/category/" + category
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-VTEX-API-AppKey": apikey,
            "X-VTEX-API-AppToken": apitoken
        }
        try:
            response = requests.get(url_complete, headers=headers)
        except ConnectionError as error:
            return Response({
                'message': 'Error',
                'errors': response.text
            }, status=status.HTTP_400_BAD_REQUEST)
        if response.status_code == 200:
            return response.json()
        else:
            return Response({
                'message': 'Error',
                'errors': response.text
            }, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def create_category(self, data, hub):
        category_id = EcommerceCategory.objects.filter(
            Q(vtex_id__iexact=str(data['Id']))
        ).first()
        if not category_id:
            vals = {
                'name': data['Name'],
                'state': 'publish',
                'platform': hub.id,
                'vtex_id': str(data['Id']),
                'keywords': data['Keywords'],
                'title': data['Title'],
                'description': data['Description'],
                'remarketing_code': data['AdWordsRemarketingCode'],
                # 'vtex_lomadee_campaign_code': data['LomadeeCampaignCode'],
                'parent': data['FatherCategoryId'] if data['FatherCategoryId'] else '',
                'global_category': data['GlobalCategoryId'],
                'showing_storefront': data['ShowInStoreFront'],
                'active': data['IsActive'],
                'store_front_link': data['ActiveStoreFrontLink'],
                'show_brand_filter': data['ShowBrandFilter'],
                'score': data['Score'] if data['Score'] else 0,
                'mtto': data['StockKeepingUnitSelectionMode'],
                'has_children': data['HasChildren'],
                'is_department': True if data['FatherCategoryId'] else False,
            }
            if data['FatherCategoryId']:
                parent_id = EcommerceCategory.objects.filter(
                    Q(vtex_id__iexact=str(data['FatherCategoryId']))
                ).first()
                vals['parent'] = parent_id.id if parent_id else None
            serializer_category = self.serializer_class(data=vals)
            if serializer_category.is_valid():
                serializer_category.save()

    def search_platform(self, data):
        platform = EcommerceHub.objects.filter(
            Q(platfrom__iexact=data)
        ).first()
        return platform

    @action(detail=False, methods=['post'])
    def get_category_vtex(self, request):
        for value in request.data['platform']:
            hub = self.search_platform(value)
            url = hub.url + "/api/catalog_system/pub/category/tree/1"
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
                    data_parent = self.get_category_info(hub.url, apikey, apitoken, category=str(data['id']))
                    self.create_category(data_parent, hub)
                    if data['hasChildren']:
                        for children in data['children']:
                            data_children = self.get_category_info(hub.url, apikey, apitoken, category=str(children['id']))
                            self.create_category(data_children, hub)
                return Response({
                    'message': 'Category creadas correctamente'
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'message': 'Error',
                    'errors': response.text
                }, status=status.HTTP_400_BAD_REQUEST)


