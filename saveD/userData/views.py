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
        customer1.location_lat = customer1.disasterIn.disasterName.encode('ascii','ignore')
        serializer =customerSerializer(customer1)
        return JsonResponse(serializer.data)


    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = customerSerializer(customer1, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customerFavouriteDetails(request, name):
    try:
        # variable to get the particular customer
        customer1 = customer.objects.get(email_id=name)

    except customer.DoesNotExist:
        return HttpResponse(status=404)

    s1 = customer1.email_id_friend_1.encode('ascii','ignore')
    s2 = customer1.email_id_friend_2.encode('ascii','ignore')
    s3 = customer1.email_id_friend_3.encode('ascii','ignore')

    customerFriendList = customer.objects.filter(email_id=s1) | customer.objects.filter(email_id=s2) |customer.objects.filter(email_id=s3)

    if request.method == 'GET':
        serializer = customerSerializer(customerFriendList, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def customerSearchDetails(request, name):
    customerSearchList = customer.objects.filter(email_id__icontains=name) | customer.objects.filter(username__icontains=name) |customer.objects.filter(blood_group__icontains=name)
    if request.method == 'GET':
        serializer = customerSerializer(customerSearchList, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def marksafe(request, name):
    try:
        # variable to get the particular customer
        customer1 = customer.objects.get(email_id=name)
    except customer.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        customer1.isPersonInTrouble = False
        customer1.save()
        serializer = customerSerializer(customer1)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def markunsafe(request, name):
    try:
        # variable to get the particular customer
        customer1 = customer.objects.get(email_id=name)
    except customer.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        customer1.isPersonInTrouble = True
        customer1.save()
        serializer = customerSerializer(customer1)
        return JsonResponse(serializer.data, safe=False)

