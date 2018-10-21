from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from userData.models import customer
from userData.serializers import customerSerializer

def index(request):
    return HttpResponse("Hello, world. Welcome to saveD")

@csrf_exempt
def customerList(request):
    #get method
    if request.method == 'GET':
        customers = customer.objects.all()
        serializer=customerSerializer(customers,many=True )
        return JsonResponse(serializer.data, safe=False)

    #post method to the customer database
    elif request.method =="POST":
        data = JSONParser().parse(request)
        serializer = customerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)