from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from hotels.models import Hotel 
from django.core import serializers

@login_required
def hotel(request):
    if request.method == 'GET':  
        if 'city_id' in request.GET:
            hotels_objects = Hotel.objects.filter(city=request.GET['city_id'])
        else:        
            hotels_objects =  Hotel.objects.all()
            hotels_objects = hotels_objects.order_by('pk')

        if 'from_id' in request.GET:
            hotels_objects = hotels_objects.filter(id__gte=request.GET['from_id'])

        if 'limit' in request.GET:
            hotels_objects = hotels_objects[:int(request.GET['limit'])]

        
        hotels_json = serializers.serialize("json", hotels_objects)
        data = {"data": hotels_json}
        return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})
