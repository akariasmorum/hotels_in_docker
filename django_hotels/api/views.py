from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from hotels.models import Hotel 
from django.core import serializers


@login_required
def hotel(request):
    if request.method == 'GET':  
        city_id = request.GET.get('city_id')
        from_id = request.GET.get('from_id')
        limit = request.GET.get('limit')
        hotels_objects = filter_hotels(city_id, limit, from_id)        
        data = serializers.serialize("json", hotels_objects)
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})


def filter_hotels(city_id=None, limit=None, from_id=None):
    hotels_objects = Hotel.objects.all()

    if from_id:
        hotels_objects = Hotel.objects.filter(id__gt=from_id)

    if city_id:
        hotels_objects = hotels_objects.filter(city=city_id)

    if limit:
        hotels_objects = hotels_objects[:int(limit)]
    
    return hotels_objects
