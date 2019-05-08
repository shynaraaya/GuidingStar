import json
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from api.serializers import *

@csrf_exempt
def hotel_lists(request):
    if request.method == 'GET':
        hotel_lists = HotelList.objects.all()
        serializer = HotelListSerializer2(hotel_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = HotelListSerializer2(data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def hotel_list_detail(request, pk):
    try:
        hotellist = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = HotelSerializer2(hotellist)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = HotelSerializer2(instance=hotellist, data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        hotellist.delete()
        return JsonResponse({'delete': True})

    return JsonResponse(hotellist.to_json())


@csrf_exempt
def flight_lists(request):
    if request.method == 'GET':
        flight_lists = Flight.objects.all()
        serializer = FlightSerializer2(flight_lists, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = FlightSerializer2(data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def flights_list_detail(request, pk):
    try:
        tasklist = Flight.objects.get(id=pk)
    except Flight.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = FlightSerializer2(tasklist)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = FlightSerializer2(instance=tasklist, data=body)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        tasklist.delete()
        return JsonResponse({'delete': True})

    return JsonResponse(tasklist.to_json())


@csrf_exempt
def flight(request, pk):
    try:
        flight_lists = Flight.objects.get(id=pk)
    except Flight.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        flight = flight_lists.task_set.all()
        serializer = FlightSerializer2(flight, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = FlightSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

@csrf_exempt
def hotel(request, pk):
    try:
        hotel_lists = Hotel.objects.get(id=pk)
    except Hotel.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        hotel = hotel_lists.task_set.all()
        serializer = HotelSerializer2(hotel, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = HotelSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

