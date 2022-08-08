from django.http import JsonResponse
from .models import Api
from .serializers import ApiSerializer
from rest_framework import generics


class Get(generics.ListAPIView):
    serializer_class = ApiSerializer
    queryset = Api.objects.all()


class Post(generics.CreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
   
class Update(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class Delete(generics.DestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer