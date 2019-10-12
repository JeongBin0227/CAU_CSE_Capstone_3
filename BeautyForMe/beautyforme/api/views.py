from accounts.models import *
from .serializer import ProfileSerializer

from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework import status

class ProfileInfo(APIView):
    # permission_classes = [IsAdminUser]
    
    def get(self, request, format=None):
        queryset = Profile.objects.filter(user=request.user)
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProfileSerializer(data=request.data)
        # print(serializer)
        # print(serializer.is_valid())
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)