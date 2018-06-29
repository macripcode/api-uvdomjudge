from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def users(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    if request.method == 'POST':
        data = request.data

        data_modified={}
        data_modified['id']=data['id']
        data_modified['password']=data['password']
        data_modified['username']=data['username']
        data_modified['first_name']=data['first_name']
        data_modified['last_name']=data['last_name']
        data_modified['email']=data['email']
        serializer = UserSerializer(data=data_modified)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=data['username'])
            token = Token.objects.create(user_id=user.id,key=data['token'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        User.objects.all().delete()
        return Response(status=status.HTTP_200_OK)
