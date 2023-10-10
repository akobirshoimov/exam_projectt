from django.shortcuts import render
from .serializers import FieldsSerializers,BronSerializers
from .models import FieldsModel,BronModel
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from .permissions import UserPermissionClass,AdminPermissionClass,OwnerPermission,AdminOrOwnerPermissionClass


# Create your views here.

# CRUD Field

class CreateFieldView(generics.CreateAPIView):
    queryset = FieldsModel.objects.all()
    serializer_class = FieldsSerializers
    permission_classes = (IsAuthenticated,AdminOrOwnerPermissionClass)

class ListFieldView(generics.ListAPIView):
    queryset = FieldsModel.objects.all()
    serializer_class = FieldsSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class DetailFieldView(generics.RetrieveAPIView):
    queryset = FieldsModel.objects.all()
    serializer_class = FieldsSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass,UserPermissionClass)

class UpdateFieldView(generics.UpdateAPIView):
    queryset = FieldsModel.objects.all()
    serializer_class = FieldsSerializers
    permission_classes = (IsAuthenticated,AdminOrOwnerPermissionClass)

class DeleteFieldsView(generics.DestroyAPIView):
    queryset = FieldsModel.objects.all()
    serializer_class = FieldsSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass,UserPermissionClass)

# CRUD Bron

class CreateBronView(generics.CreateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass,UserPermissionClass)

class ListBronView(generics.ListAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (IsAuthenticated,AdminOrOwnerPermissionClass)

class DetailBronView(generics.RetrieveAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class UpdateBronView(generics.UpdateAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (IsAuthenticated,AdminPermissionClass)

class DeleteBronView(generics.DestroyAPIView):
    queryset = BronModel.objects.all()
    serializer_class = BronSerializers
    permission_classes = (IsAuthenticated,AdminOrOwnerPermissionClass)

    
# Bron qilinmagan vaqtlarni olish

# class UnbronTimeView(APIView):
#     def get(self,request):
#         if request.user != 'AnonymousUser':
#             if request.user.roles == 3:
#                 detail = BronModel.objects.filter(unbron_time=request.data)
#                 serializer = BronSerializers(detail,many = True)
#                 if serializer.is_valid():
#                     return Response(serializer.data)
#                 return Response(serializer.errors)
#             return Response('you cannot read info')
#         return Response('you cannot read info')
    








    












