from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from webapp.logic import ChickenLogic
from webapp.models import SensorData
from webapp.utils import sunrise_and_sunset_for_date, our_json_dumps


def _populate_basic_data():
    latest_read = SensorData.objects.last()
    sunrise, sunset = sunrise_and_sunset_for_date()
    chicken_status = ChickenLogic.evaluate_situation()
    data = {'chickens_put_away': not latest_read.door_open,
            'last_updated': latest_read.timestamp, 'sunrise': sunrise, 'sunset': sunset,
            'message': chicken_status.message}
    return data


def index(request):
    context = RequestContext(request, _populate_basic_data())

    return render(request, 'webapp/index.html', context)

    # latest_sensor_reads = SensorData.objects.all()[:10]
    # output = ', '.join(["%s" % (s.timestamp) for s in latest_sensor_reads])
    # return HttpResponse(output)


@csrf_exempt
def add_data(request):
    data_string = request.body
    try:
        s = SensorData.create_from_string(data_string)
        s.save()
        return HttpResponse('OK')
    except Exception as e: # TODO: catch a more specific exception
        return HttpResponse(e, status=400)


@csrf_exempt
def data(request):
    json_data = our_json_dumps(_populate_basic_data())
    return HttpResponse(json_data)