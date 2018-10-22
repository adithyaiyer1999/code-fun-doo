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

@csrf_exempt
def customerDetails(request, name):
    if customer.objects.filter(email_id = name).exists():
        customer1 = customer.objects.get(email_id = name)

    else:
        if request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = customerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)


    #get method to get the tasks associated with a customer as json
    if request.method == 'GET':
        serializer =customerSerializer(customer1)
        return JsonResponse(serializer.data)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = customerSerializer(customer1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)



