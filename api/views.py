from django.http import JsonResponse
from .models import Api
from .serializers import ApiSerializer


def api_list (request):
    #get all the drinks
    api = Api.objects.all()
  
    #serialize them
    serializer = ApiSerializer(api, many=True)
    #return jason
    return JsonResponse(serializer.data , safe=False)