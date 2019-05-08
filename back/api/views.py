from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

from .models import User, Flight, Hotel

@csrf_exempt
def index(request):
	if request.method == 'POST':
		secret = data['secret']
		source = request.POST['source']
		sourceArr = source.split(',')
		sourceCity = sourceArr[0]
		destination = request.POST['destination']
		destinationArr = destination.split(',')
		destinationCity = destinationArr[0]
		startdate = request.POST['startdate']
		startdate = startdate.split('-')
		year = int(startdate[0])
		month = int(startdate[1])
		day = int(startdate[2])
		flightClass = request.POST['class']
		print(request.POST)
		if (flightClass == 'economy'):
			flights = Flight.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingEconomy__gt=0)
			flights = list(flights)
			return render(request, 'index.html',{"results":"yes", "some_list": flights, "class":flightClass})
		elif (flightClass == 'business'):	
			flights = Flight.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingBusiness__gt=0)
			flights = list(flights)
			return render(request, 'index.html',{"results":"yes", "some_list": flights, "class":flightClass})
		else:
			flights = Flight.objects.filter(sourceLocation = sourceCity).filter(destinationLocation=destinationCity).filter(departureDate=datetime.date(year,month,day)).filter(numSeatsRemainingFirst__gt=0)
			flights = list(flights)
			return render(request, 'index.html',{"results":"yes", "some_list": flights, "class":flightClass})
	else:
		return render(request, 'index.html')