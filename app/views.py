from django.http import HttpResponse
from django.shortcuts import render
from app.models import Scooter
import datetime
import json
from django.core import serializers

now = datetime.datetime.now()

def home(request):
    return render(request, 'home.html')

def get_scooter(request):
    current_date_time = now.isoformat()
    #scooter = Scooter.objects.get(time=current_date_time)
    scooter = Scooter.objects.all()
    #data = json.dumps(scooter)
    data = serializers.serialize('json', scooter)
    return HttpResponse(data, content_type='application/json')